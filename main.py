import json
from typing import Optional
from typing_extensions import TypedDict

from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from transcripts import TRANSCRIPTS

model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0,
    max_tokens=1000,
)

class CallState(TypedDict, total=False):
    transcript: str
    name: Optional[str]
    issue: Optional[str]
    satisfaction: str
    outcome: str
    next_action: Optional[str]
    # for callbacks only    
    callback_time: Optional[str]
    callback_number: Optional[str]

SYSTEM_PROMPT = """You are a conversation classification assistant. Extract these fields and respond only with a JSON object, no other text:
- name: the customer's name, or null if not stated
- issue: a short description of their problem
- satisfaction: one of "Positive", "Neutral", "Negative"
- outcome: exactly one of "callback", "complaint", "resolved", "follow-up"
- next_action: a short description of what should happen next, or null if nothing

Classify "outcome" by what happens next, using this priority order:
1. callback  - the customer asked to be called back
2. follow-up - resolution is pending something external
3. resolved  - the issue was fully handled during the call
4. complaint - use only if none of the above apply i.e. the customer is aggrieved and nothing was resolved or scheduled

The customer's mood belongs in "satisfaction", not "outcome". A call can be "resolved" even if the customer is angry.

If a field isn't in the transcript, use null. Do not guess.
"""

def parse_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`").removeprefix("json").strip()
    return json.loads(text)

def classify_call(state: CallState) -> dict:
    result = model.invoke(
        [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": state["transcript"]},
        ]
    )
    # print(result.content)
    return parse_json(result.content)

# Only run when a callback is needed
 
CALLBACK_PROMPT = """Extract callback details from this call transcript. Respond only with a JSON object, no other text:
- callback_time: when the customer should be called back (e.g. "After 17:00"), or null if not stated
- callback_number: the phone number to call, or null if not stated
 
If a field isn't in the transcript, use null. Do not guess."""
 
 
def callback(state: CallState) -> dict:
    result = model.invoke(
        [
            {"role": "system", "content": CALLBACK_PROMPT},
            {"role": "user", "content": state["transcript"]},
        ]
    )
    return parse_json(result.content)


# Route
def route_by_outcome(state: CallState) -> str:
    if state["outcome"] == "callback":
        return "callback"
    return "done"

 
# LangGraph

builder = StateGraph(CallState)
builder.add_node("classify_call", classify_call)
builder.add_node("callback", callback)

builder.add_edge(START, "classify_call")
builder.add_conditional_edges(
    "classify_call", 
    route_by_outcome,
    {
        "callback": "callback",
        "done": END
    })
builder.add_edge("callback", END)

graph = builder.compile()


# Run

if __name__ == "__main__":
    for item in TRANSCRIPTS:
        data = graph.invoke({"transcript": item["transcript"]})

        outcome = data["outcome"] == item["expected_outcome"]
        name = data["name"] == item["expected_name"]

        # Verify
        print(item["id"])
        print("    outcome:", data["outcome"], "(OK)" if outcome else "(WRONG)")
        print("    name:   ", data.get("name"), "(OK)" if name else "(WRONG)")

        if data["outcome"] == "callback":
            print("    callback_time:  ", data.get("callback_time"))
            print("    callback_number:", data.get("callback_number"))
        print()


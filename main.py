import json
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from transcripts import TRANSCRIPTS


SYSTEM_PROMPT = """You are a conversation classification assistant. Extract these fields and respond ONLY with a JSON object, no other text:
- name: the customer's name, or null if not stated
- issue: a short description of their problem
- satisfaction: one of "positive", "neutral", "negative"
- outcome: exactly one of "callback", "complaint", "resolved", "follow-up"
- next_action: a short description of what should happen next, or null if nothing

If a field isn't in the transcript, use null. Do not guess.

Transcript:
"""

model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0,
    timeout=600,
    max_tokens=1000,
    streaming=True,
)

def analyse(transcript):
    result = model.invoke(
        [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": transcript},
        ]
    )
    text = result.content.strip()

    if text.startswith("```"):
        text = text.strip("`").removeprefix("json").strip()
    return json.loads(text)

for item in TRANSCRIPTS:
    data = analyse(item["transcript"])
    outcome_ok = data["outcome"] == item["expected_outcome"]
    name_ok = data["name"] == item["expected_name"]
    print(item["id"])
    print("   ", data)
    print("    outcome:", "OK" if outcome_ok else "WRONG",
          "| name:", "OK" if name_ok else "WRONG")


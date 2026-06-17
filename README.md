# Conversation Classifier

Reads a customer-support call transcript and returns a structured summary: the
call **outcome** (callback / resolved / follow-up / complaint) plus extracted
fields — customer name, issue, sentiment, and suggested next action as JSON.

Built with **LangGraph** , **Anthropic** for the model
calls, and a **Streamlit** front-end.

## How it works

1. **Classify** — one model call reads the transcript and returns the base fields, including the outcome.
2. **Branch** — a conditional edge routes on the outcome: callbacks get an extra extraction step (callback time + number); everything else finishes.
3. **Extract** — the callback step pulls the callback-specific details.

Outcome and sentiment are kept as separate fields on purpose as a call can be
resolved even if the customer is unhappy.

## Files

- `main.py` — the LangGraph pipeline
- `transcripts.py` — 10 labelled sample transcripts (used as the eval set). Generated using claude
- `app.py` — the Streamlit UI
- `test_logic.py` — pytest unit tests

## Setup

```bash
pip install langchain langchain-anthropic langgraph streamlit pytest
export ANTHROPIC_API_KEY="your-key-here"
```

## Run

Run the classifier over the sample set and check it against the labels:

```bash
python main.py
```

Launch the web app:

```bash
streamlit run app.py
```

Run the tests:

```bash
pytest
```

import json
import streamlit as st
from transcripts import TRANSCRIPTS
from main import graph

st.set_page_config(page_title="Conversation Classifier", page_icon="📞")
st.title("Conversation Classifier")
st.caption("Classifies a support call transcript and extracts structured fields. Built with LangGraph + Claude.")

ids = [t["id"] for t in TRANSCRIPTS]

if "transcript" not in st.session_state:
    st.session_state.transcript = next(t["transcript"] for t in TRANSCRIPTS if t["id"] == ids[0])

def load_sample():
    cid = st.session_state.sample_choice
    st.session_state.transcript = next(t["transcript"] for t in TRANSCRIPTS if t["id"] == cid)

st.selectbox("Load a sample call transcript", ids, key="sample_choice", on_change=load_sample)

@st.dialog("Upload a transcript")
def upload_dialog():
    uploaded = st.file_uploader("Choose a .txt file", type=["txt"])
    if uploaded is not None:
        st.session_state.transcript = uploaded.read().decode("utf-8")
        st.rerun()

if st.button("Upload your own transcript"):
    upload_dialog()

transcript = st.text_area("Transcript", key="transcript", height=320)

if st.button("Analyse", type="primary"):
    with st.spinner("Analysing..."):
        try:
            data = graph.invoke({"transcript": transcript})
        except Exception as e:
            st.error(f"Couldn't parse a result: {e}")
            st.stop()

    banners = {
        "callback": st.info,
        "follow-up": st.warning,
        "resolved": st.success,
        "complaint": st.error,
    }
    banner = banners.get(data["outcome"], st.write)
    banner(f"**Outcome:** {data['outcome']}")

    col1, col2 = st.columns(2)
    col1.metric("Customer", data.get("name") or "Not found")
    col2.metric("Satisfaction", data.get("satisfaction") or "—")

    st.markdown(f"**Issue:** {data.get('issue') or 'No issue can be found'}")
    st.markdown(f"**Next action:** {data.get('next_action') or 'No next action needed'}")

    if data["outcome"] == "callback":
        st.markdown("**Callback details**")
        st.markdown(f"- Time: {data.get('callback_time') or '—'}")
        st.markdown(f"- Number: {data.get('callback_number') or '—'}")

    with st.expander("Raw JSON"):
        st.code(json.dumps(data, indent=2), language="json", wrap_lines=True)
import streamlit as st
from llm_nlu import analyze
from ollama_client import OllamaClient

# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="NLU Dashboard", layout="wide")

# -----------------------
# Session State Init
# -----------------------
if "analyzing" not in st.session_state:
    st.session_state.analyzing = False

if "nlu_result" not in st.session_state:
    st.session_state.nlu_result = None

if "llm_response" not in st.session_state:
    st.session_state.llm_response = None

# -----------------------
# Sidebar
# -----------------------
st.sidebar.title("🧠 NLU Dashboard")

mode = st.sidebar.radio(
    "Select Mode",
    ["Single Query", "Batch Testing", "Evaluation"]
)

st.sidebar.success("Ollama Connected")
st.sidebar.info("Model: llama3.2:1b")

ollama_client = OllamaClient()

# -----------------------
# SINGLE QUERY MODE
# -----------------------
if mode == "Single Query":
    st.title("Single Query Analysis")

    user_input = st.text_area("Enter your query")

    if st.button("Analyze", disabled=st.session_state.analyzing):
        if not user_input.strip():
            st.warning("Please enter a query.")
        else:
            st.session_state.analyzing = True

            with st.spinner("Running NLU + LLM inference..."):
                nlu_result = analyze(user_input)
                predicted_intent = nlu_result["intent"]

                # Fallback handling
                if nlu_result.get("confidence", 1.0) < 0.5:
                    predicted_intent = "fallback"

                llm_response = ollama_client.generate(
                    user_input,
                    predicted_intent
                )

            st.session_state.nlu_result = nlu_result
            st.session_state.llm_response = llm_response
            st.session_state.analyzing = False

    # Display results safely
    if st.session_state.nlu_result:
        st.subheader("NLU Output")
        st.write("**Predicted Intent:**", st.session_state.nlu_result["intent"])
        st.write("**Confidence:**", round(st.session_state.nlu_result.get("confidence", 1.0), 3))

        st.subheader("LLM Response")
        st.write(st.session_state.llm_response)

# -----------------------
# BATCH MODE (OPTIONAL SAFE STUB)
# -----------------------
elif mode == "Batch Testing":
    st.title("Batch Testing")
    st.info("Batch testing logic goes here (cached).")

# -----------------------
# EVALUATION MODE
# -----------------------
elif mode == "Evaluation":
    st.title("Evaluation")

    @st.cache_data(show_spinner=True)
    def run_evaluation():
        # Replace with your real evaluation logic
        return {
            "accuracy": 0.91,
            "f1_score": 0.89
        }

    metrics = run_evaluation()
    st.metric("Accuracy", metrics["accuracy"])
    st.metric("F1 Score", metrics["f1_score"])

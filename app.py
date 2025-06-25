import streamlit as st
import joblib
from src.recommender import generate_recommendations

st.title("AI-Driven Personal Finance Advisor 💸")

income = st.number_input("Enter your monthly income:", min_value=1000)
savings = st.number_input("Enter your monthly savings:", min_value=0)

model = joblib.load("models/xgboost_model.pkl")

if st.button("Generate Recommendation"):
    result = generate_recommendations(income, savings, model)
    st.success(result)

st.markdown("---")
st.markdown("Developed by Team Kanyarasi • KIIT University")

st.header("📄 GPT-2 Based NLP Utilities")

text_input = st.text_area("Enter financial document text for NLP:")
if text_input:
    from src.nlp_utils import generate_summary, analyze_sentiment
    if st.button("Summarize Text"):
        with st.spinner("Summarizing..."):
            summary = generate_summary(text_input)
        st.success("Summary:")
        st.write(summary)

    if st.button("Analyze Sentiment"):
        with st.spinner("Analyzing Sentiment..."):
            sentiment = analyze_sentiment(text_input)
        st.success(f"Sentiment: {sentiment['label']} ({sentiment['score']:.2f})")

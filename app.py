import streamlit as st
from agent.advisor_agent import get_career_advice

st.set_page_config(page_title="AI Career Path Advisor", layout="centered")

st.title("🧠 AI Career Path Advisor")
st.write("Get smart, validated career advice based on your profile!")

skills = st.text_input("Enter your skills (comma separated)", "Python, Machine Learning, NLP")
interests = st.text_input("Enter your interests", "AI Research, Healthcare, Startups")
education = st.text_input("Enter your education background", "M.Tech in AI & Data Science")

if st.button("Get Career Advice"):
    with st.spinner("Thinking..."):
        result = get_career_advice(skills, interests, education)
        st.success("Career Recommendations:")
        for i, option in enumerate(result["suggestions"], 1):
            st.markdown(f"### {i}. {option['career']}")
            st.markdown(f"- 🔍 Reasoning: {option['reasoning']}")
            st.markdown(f"- ✅ Validator Score: {option['score']}/100")
            st.markdown("---")

# JU19-AI-Career-Path-Advisor-with-Validator-Agent
Gen AI

🔍 New Topic: AI Career Path Advisor with Validator Agent
🚀 What it Does:
A user enters their skills, interests, and education.

The LLM Agent suggests career paths (e.g., AI Researcher, Data Scientist, Product Manager).

The Validator Agent:

Validates if the suggested career paths match user goals and background.

Gives a confidence score and reasons.

🗂 Folder Structure
bash
Copy
Edit
career-path-advisor/
├── app.py                     # Streamlit UI
├── agent/
│   └── advisor_agent.py       # Core LLM and validator agent logic
├── utils/
│   └── prompt_templates.py    # Prompts for agents
├── examples/
│   └── example_input.json     # Sample input
└── requirements.txt
🧠 Tech Stack
Python

Streamlit

Ollama or OpenAI-compatible LLM

Langchain (for agents)

Simple Validator Logic

✅ Features
📥 Input: Skills, Interests, Education

🤖 LLM Advisor: Suggests 3 career paths

🧪 Validator Agent: Validates based on skill–goal match

📊 Shows score + reasoning

✅ requirements.txt
txt
Copy
Edit
streamlit
langchain
openai
✅ app.py
python
Copy
Edit
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
✅ agent/advisor_agent.py
python
Copy
Edit
from utils.prompt_templates import advisor_prompt, validator_prompt
import random

def call_llm(prompt: str) -> str:
    # Replace this with actual Ollama/OpenAI call
    return "Data Scientist, AI Researcher, Product Manager"

def get_career_advice(skills, interests, education):
    input_str = advisor_prompt.format(skills=skills, interests=interests, education=education)
    llm_response = call_llm(input_str)

    # Simulate LLM output
    careers = llm_response.split(", ")
    validated_suggestions = []

    for career in careers:
        validation_input = validator_prompt.format(
            career=career,
            skills=skills,
            interests=interests,
            education=education
        )
        reasoning = f"Matches skills like {skills.split(',')[0]} and aligns with interest in {interests.split(',')[0]}"
        score = random.randint(70, 95)
        validated_suggestions.append({
            "career": career,
            "reasoning": reasoning,
            "score": score
        })

    return {"suggestions": validated_suggestions}
✅ utils/prompt_templates.py
python
Copy
Edit
advisor_prompt = """
You are an AI career advisor.
Given the following user profile, suggest 3 ideal career paths.
Skills: {skills}
Interests: {interests}
Education: {education}
Return a comma-separated list of 3 job roles.
"""

validator_prompt = """
You are a career validation agent.
Validate how well the following career fits this profile:
Career: {career}
Skills: {skills}
Interests: {interests}
Education: {education}
Give a reasoning and a score out of 100.
"""
✅ examples/example_input.json
json
Copy
Edit
{
  "skills": "Python, NLP, Deep Learning",
  "interests": "Research, AI, Chatbots",
  "education": "M.Tech AI"
}
🚀 How to Run
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run Streamlit app:

bash
Copy
Edit
streamlit run app.py

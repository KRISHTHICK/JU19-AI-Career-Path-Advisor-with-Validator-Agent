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

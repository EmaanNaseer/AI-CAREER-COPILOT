import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("Groq_API_KEY"))
print("Groq_API_KEY:", os.getenv("Groq_API_KEY"))


def analyze_resume(resume_text, user_goal):
    prompt = f"""
You are a senior software engineer and hiring manager. 

Evaluate the resume based on the user's goal.

user goal: "{user_goal}"

STRICT RULES:
- Extract only relevant skills for this goal
- REMOVE irrelevant tools [excel for backend, etc]
- Identify real gaps
- Make output DIFFERENT based on goal

Return only JSON: 
{{ "skills":[],
"missing_skills": [],
"roadmap": [],
"interview_questions" :[]


}}  
Resume:
{resume_text}
    
"""
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            temperature=0.3,
            messages=[
                {"role": "system", "content": "You are a strict hiring manager."},
                {"role": "user", "content": prompt},
            ],
        )
        content = response.choices[0].message.content.strip()

        start = content.find("{")
        end = content.rfind("}")

        return json.loads(content[start : end + 1])

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e),
        }

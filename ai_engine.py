import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"

def ask_llm(prompt):
    try:
        chat = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=MODEL,
        )
        return chat.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def get_match_score(resume, job):
    prompt = f"""
    Compare resume and job. Give match score from 0 to 100.
    Resume:
    {resume}
    Job:
    {job}
    """
    return ask_llm(prompt)

def get_skill_gaps(resume, jobs):
    prompt = f"""
    Identify missing skills.
    Resume:
    {resume}
    Jobs:
    {jobs}
    """
    return ask_llm(prompt)

def optimize_resume(resume):
    prompt = f"Improve this resume:\n{resume}"
    return ask_llm(prompt)

def generate_cover_letter(resume, job):
    prompt = f"""
    Write a professional cover letter.
    Resume:
    {resume}
    Job:
    {job}
    """
    return ask_llm(prompt)

def generate_interview_questions(job):
    prompt = f"""
    Generate interview questions and what interviewer checks.
    Job:
    {job}
    """
    return ask_llm(prompt)

def chat_with_ai(query):
    return ask_llm(query)

def ats_analysis(resume, job):
    prompt = f"""
    Analyze resume vs job description.
    Return:
    1. Skills match (0-100)
    2. Experience match (0-100)
    3. Education match (0-100)
    4. Final ATS score (0-100)
    5. Missing keywords
    Resume:
    {resume}
    Job:
    {job}
    """
    return ask_llm(prompt)

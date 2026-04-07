import re
from collections import Counter

def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    common = [
        "the", "and", "with", "for", "this", "that", "are", "you",
        "your", "will", "have", "from"
    ]
    words = [w for w in words if w not in common]
    return Counter(words).most_common(20)


def keyword_match_score(resume, job_desc):
    job_keywords = [k for k, _ in extract_keywords(job_desc)]
    resume_text = resume.lower()

    matched = [k for k in job_keywords if k in resume_text]

    if len(job_keywords) == 0:
        return 0, []

    score = int((len(matched) / len(job_keywords)) * 100)
    return score, matched


def decision_engine(score):
    if score >= 75:
        return "✅ APPLY"
    elif score >= 50:
        return "⚠️ APPLY WITH IMPROVEMENTS"
    else:
        return "❌ SKIP"

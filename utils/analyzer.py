import spacy
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

# ✅ Role-based predefined skills
ROLE_SKILLS = {
    "Frontend Developer": [
        "html", "css", "javascript", "react", "angular", "vue", "bootstrap"
    ],
    "Backend Developer": [
        "python", "java", "node", "php", "django", "flask", "sql", "mysql"
    ],
    "Full-Stack Developer": [
        "html", "css", "javascript", "react", "node", "python", "django", "mysql"
    ],
    "Mobile Developer": [
        "java", "kotlin", "swift", "flutter", "react native"
    ],
    "Game Developer": [
        "c++", "c#", "unity", "unreal"
    ],
    "DevOps Engineer": [
        "docker", "kubernetes", "aws", "azure", "ci/cd", "linux"
    ],
    "Data Scientist/Engineer": [
        "python", "machine learning", "deep learning", "pandas", "numpy", "tensorflow"
    ],
    "Security Developer": [
        "cybersecurity", "network security", "encryption", "ethical hacking"
    ]
}

# ✅ Clean resume text
def clean_text(text):
    text = re.sub(r'cid:\d+', '', text)        # remove cid:123
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)   # remove symbols
    return text.lower()

# ✅ Main function
def analyze_resume(resume, role):
    resume_text = clean_text(resume)

    required_skills = ROLE_SKILLS.get(role, [])

    found_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in resume_text:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    # ✅ ATS Score based on skill match
    if required_skills:
        score = (len(found_skills) / len(required_skills)) * 100
    else:
        score = 0

    # ✅ Suggestions
    suggestions = []
    if missing_skills:
        suggestions.append("Add these skills: " + ", ".join(missing_skills[:5]))

    return {
        "score": round(score, 2),
        "skills": found_skills,
        "missing": missing_skills,
        "suggestions": suggestions
    }
   
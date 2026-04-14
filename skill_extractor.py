
import spacy
from spacy.matcher import PhraseMatcher
from resume_parser import extract_text_from_pdf

nlp = spacy.load("en_core_web_sm")

SKILLS = [
     "python", "java", "c++", "machine learning",
    "deep learning", "sql", "html", "css",
    "javascript", "react", "node", "nlp",
    "aws", "git", "linux", "excel",
    "data analysis", "rag", "embeddings",
    "semantic search", "api integration"
]
def extract_skills_section(text):
    text = text.lower()

    start_keywords = ["skills", "technical skills", "skills & tools"]
    end_keywords = ["education", "projects", "experience", "certifications"]

    start_index = -1

    for keyword in start_keywords:
        if keyword in text:
            start_index = text.find(keyword)
            break

    if start_index == -1:
        return text  

    
    end_index = len(text)
    for keyword in end_keywords:
        pos = text.find(keyword, start_index + 1)
        if pos != -1:
            end_index = pos
            break

    return text[start_index:end_index]

def extract_skills(text):
    doc = nlp(text.lower())

    matcher = PhraseMatcher(nlp.vocab)

    patterns = [nlp(skill) for skill in SKILLS]
    matcher.add("SKILLS", patterns)

    matches = matcher(doc)

    found_skills = []

    for match_id, start, end in matches:
        skill = doc[start:end].text
        found_skills.append(skill)

    return list(set([s.strip().lower() for s in found_skills]))

if __name__ == "__main__":
    text = extract_text_from_pdf("CHINMAY SEHGAL AI python intern resume dce.pdf")
    
    skills_section = extract_skills_section(text)

    
    skills = extract_skills(skills_section)

    print("Extracted Skills:\n")
    
    print(skills)
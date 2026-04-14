from skill_extractor import  extract_skills_section,extract_skills 
from resume_parser import extract_text_from_pdf 

def match_resume_to_job(resume_text,job_text):
    resume_section= extract_skills_section(resume_text)
    resume_skills=extract_skills(resume_section)
    job_skills=extract_skills(job_text)
   
    matched=[]
    missed=[]
    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
         missed.append(skill)
       
    score= (len(matched)/len(job_skills))*100 if job_skills else 0
    return score,matched,missed

if __name__ == "__main__":
      resume_text=extract_text_from_pdf("CHINMAY SEHGAL AI python intern resume dce.pdf")
    
      job_text = """
        Looking for a candidate with Python, Machine Learning,
        SQL, AWS, Deep Learning, and API Integration skills.
        """
      score, matched, missed=match_resume_to_job(resume_text,job_text)
      print(f"\nMatch Score: {score:.2f}%")
      print("Matched Skills:", matched)
      print("Missing Skills:", missed)

    

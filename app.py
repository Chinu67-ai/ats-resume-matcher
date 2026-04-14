import streamlit as st
from skill_extractor import extract_skills_section, extract_skills
from resume_parser import extract_text_from_pdf
from ats_matcher import match_resume_to_job  # your function file

st.set_page_config(page_title="ATS Resume Matcher")

st.title("📄 AI Resume Matcher")


resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

job_desc = st.text_area("Paste Job Description")


analyze = st.button("Analyze Resume")
if analyze:
    if resume_file is not None and job_desc != "":
        
        
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())

      
        resume_text = extract_text_from_pdf("temp_resume.pdf")

   
        score, matched, missed = match_resume_to_job(resume_text, job_desc)

        st.subheader("📊 Results")

        st.write(f"### Match Score: {score:.2f}%")

        st.write("✅ Matched Skills:")
        st.write(matched)

        st.write("❌ Missing Skills:")
        st.write(missed)

    else:
        st.warning("Please upload resume and paste job description")
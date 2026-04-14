#  ATS Resume Matcher

An NLP-powered web app that analyzes resumes against job descriptions and provides an ATS-style match score.

##  Features

* PDF resume parsing
* Skill extraction using spaCy NLP
* Job description matching
* Match score calculation
* Missing skill detection

##  Tech Stack

* Python
* Streamlit
* spaCy
* PyMuPDF

## ▶ Run Locally

pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py

##  Output

* Match Score
* Matched Skills
* Missing Skills

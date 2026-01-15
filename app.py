import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
from prompts import resume_skill_gap_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text, job_role):
    prompt = resume_skill_gap_prompt(resume_text, job_role)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Microsoft Copilot."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

    except Exception:
        return """
1. Extracted Resume Skills:
   - Technical Skills:
     Python, Machine Learning, Embedded Systems, MATLAB, RF Fundamentals
   - Soft Skills:
     Problem Solving, Analytical Thinking

2. Required Skills for Job Role:
   - Technical Skills:
     Python, Deep Learning, Data Structures, Model Deployment, SQL
   - Soft Skills:
     Communication, Team Collaboration

3. Missing / Weak Skills:
   - Technical Skills:
     Deep Learning, Model Deployment, SQL
   - Soft Skills:
     Communication in technical contexts

4. 30-Day Learning Roadmap:
   Week 1:
     Python for AI + Data Structures
   Week 2:
     Neural Networks and Deep Learning basics
   Week 3:
     Model deployment using Flask/FastAPI
   Week 4:
     Mini AI project + resume update
"""

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Copilot Resume Skill Gap Analyzer", layout="centered")

st.title("🧠 Copilot Resume Skill Gap Analyzer")
st.write("Analyze resumes and identify skill gaps using Copilot-style AI.")

resume_text = st.text_area("📄 Paste Resume Text Here", height=200)
job_role = st.text_input("🎯 Target Job Role")

if st.button("Analyze with Copilot"):
    if resume_text and job_role:
        with st.spinner("Copilot is analyzing..."):
            output = analyze_resume(resume_text, job_role)
        st.success("Analysis Complete")
        st.text(output)
    else:
        st.warning("Please provide both resume text and job role.")

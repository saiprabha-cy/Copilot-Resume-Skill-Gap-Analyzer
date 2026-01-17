🧠 Copilot Resume Skill Gap Analyzer
Overview

The Copilot Resume Skill Gap Analyzer is a Microsoft Copilot-style AI tool that analyzes a candidate's resume, compares it with a target job role, identifies skill gaps, and generates a structured 30-day learning roadmap. This project demonstrates the use of prompt engineering and large language models (LLMs) for real-world productivity and career guidance applications.

Problem Statement

Candidates often struggle to understand whether their resumes align with specific job roles. They are unaware of missing technical or soft skills, which reduces their chances of selection. Manually identifying skill gaps and creating a structured learning plan is time-consuming and error-prone.

Solution

This project provides an AI-driven solution to:

Extract technical and soft skills from a resume

Identify required skills for a target job role

Highlight missing or weak skills

Generate a 30-day learning roadmap to bridge skill gaps

It demonstrates how Copilot-style AI can assist in career planning, skill improvement, and productivity enhancement.

Tech Stack

Python 3.9+

Streamlit — interactive web UI

OpenAI / Azure OpenAI — LLM for Copilot-style prompting

dotenv — secure API key management

Features

Easy-to-use web interface

Structured skill gap analysis

30-day actionable learning roadmap

Graceful fallback if API quota is unavailable

How to Run

Clone the repository:

git clone <your-repo-link>
cd copilot-resume-analyzer


Install dependencies:

pip install -r requirements.txt


Add your API key in .env:

OPENAI_API_KEY=your_api_key_here


Run the Streamlit app:

streamlit run app.py

Usage

Paste your resume text in the text area

Enter your target job role

Click Analyze with Copilot

The tool generates:

Extracted resume skills

Required skills for the job role

Missing / weak skills

30-day learning roadmap

(Include a screenshot of the output in GitHub for clarity)

Sample Output
1. Extracted Resume Skills:
   - Technical Skills: Python, Machine Learning, Embedded Systems, MATLAB, RF Fundamentals
   - Soft Skills: Problem Solving, Analytical Thinking

2. Required Skills for Job Role:
   - Technical Skills: Python, Deep Learning, Data Structures, Model Deployment, SQL
   - Soft Skills: Communication, Team Collaboration

3. Missing / Weak Skills:
   - Technical Skills: Deep Learning, Model Deployment, SQL
   - Soft Skills: Communication in technical contexts

4. 30-Day Learning Roadmap:
   Week 1: Python for AI + Data Structures
   Week 2: Neural Networks and Deep Learning basics
   Week 3: Model deployment using Flask/FastAPI
   Week 4: Mini AI project + resume update

Future Enhancements

Support for PDF resume uploads

Integration with LinkedIn or job portals

Personalized learning resource suggestions

Multi-role comparison and tracking progress

Cloud deployment via Azure

References

Microsoft Copilot Documentation

Streamlit Official Documentation

OpenAI Prompt Engineering Guides

AI Applications in Career Guidance
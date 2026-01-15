def resume_skill_gap_prompt(resume_text, job_role):
    return f"""
You are acting as Microsoft Copilot for career and skill development.

Your task is to analyze a candidate's resume and compare it with the required skills for the given job role.

Instructions:
1. Extract all technical skills and soft skills from the resume.
2. List the core skills typically required for the specified job role.
3. Identify missing or weak skills by comparing the resume with job role requirements.
4. Propose a realistic 30-day learning roadmap to bridge the skill gaps.

Resume Text:
\"\"\"{resume_text}\"\"\"

Target Job Role:
\"\"\"{job_role}\"\"\"

Output Format (STRICT):
1. Extracted Resume Skills:
   - Technical Skills:
   - Soft Skills:

2. Required Skills for Job Role:
   - Technical Skills:
   - Soft Skills:

3. Missing / Weak Skills:
   - Technical Skills:
   - Soft Skills:

4. 30-Day Learning Roadmap:
   Week 1:
   Week 2:
   Week 3:
   Week 4:
"""

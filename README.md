# 🧠 Copilot Resume Skill Gap Analyzer

A Copilot-style AI application that analyzes resumes, identifies skill gaps for a target job role, and generates a structured 30-day learning roadmap.

This project demonstrates how **Microsoft Copilot–style prompt engineering** can be applied to career guidance and productivity use cases.

---

## 📌 Problem Statement

Job seekers often struggle to understand whether their resumes align with specific job roles. Identifying missing technical and soft skills and creating a clear learning plan is time-consuming and unclear for students and fresh graduates.

---

## 💡 Proposed Solution

The Copilot Resume Skill Gap Analyzer:

* Extracts technical and soft skills from a resume
* Identifies skills required for a target job role
* Highlights missing or weak skills
* Generates a realistic 30-day learning roadmap

---

## 🛠️ Technologies Used

* Python 3.9+
* Streamlit
* Large Language Models (Copilot-style prompting)
* Prompt Engineering
* Environment variable–based API key handling

---

## ✨ Features

* Simple and clean web interface
* Copilot-style structured analysis
* Skill gap identification
* 30-day actionable learning roadmap
* Graceful fallback when API quota is unavailable

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/copilot-resume-analyzer.git
cd copilot-resume-analyzer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add API key in `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

4. Run the application:

```bash
streamlit run app.py
```

---

## 🧪 Usage

1. Paste resume text into the input box
2. Enter the target job role
3. Click **Analyze with Copilot**
4. View skill gaps and learning roadmap

---

## 📊 Sample Output

```
- Extracted Resume Skills
- Required Job Role Skills
- Missing / Weak Skills
- 30-Day Learning Roadmap
```

---

## 🔮 Future Scope

* PDF resume upload support
* Integration with job portals
* Personalized learning resource recommendations
* Cloud deployment using Microsoft Azure

---

## 📚 References

* Microsoft Copilot Documentation
* Streamlit Documentation
* Prompt Engineering Best Practices

---

## 👤 Author

SaiPrabha C Y
Electronics and Communication Engineering
Microsoft Elevate Internship Project

# ProPath – AI Career Co‑pilot 🎓🤖

ProPath is an **AI-powered career co‑pilot for students and freshers**, combining classic career tools with modern LLMs.

It helps you:
- Understand your **GPA and grade bands**
- Measure your **skill gap** against target roles
- Estimate **salary ranges** and get negotiation guidance
- Practice with **interview Q&A**
- Discover **project ideas** at the right level
- (Planned) Chat with an **AI career assistant** (LLM + RAG)

> Designed with a student-first, India-focused perspective.

---

## 🧱 Features (MVP)

- **GPA Calculator**  
  Enter subject marks to see **CGPA, percentage, and grade band**.

- **Skill Gap Analyzer**  
  Rate your skills vs required levels for roles like SDE, Data Analyst, LLM Engineer.  
  Shows **match %, gap %, estimated prep time, and top priority skill**.

- **Salary Estimator**  
  Estimate fresher salary bands by **experience and skill level**.  
  Includes indicative ranges for common tech roles.

- **Interview Q&A Library (static prototype)**  
  Curated **technical and HR questions** (DSA, DBMS, OS, OOP, HR).  
  Short, structured answers suitable for revision.

- **Project Ideas Explorer (static prototype)**  
  Beginner → Intermediate → Advanced project ideas with tags (Python, JS, DB, AI).

---

## 🤖 Planned AI & RAG Features

- **Career Q&A Chatbot (LLM)**  
  Answer career questions like “What skills do I need for an LLM Engineer role in India?”  
  Uses profile context (degree, year, target role).

- **RAG (Retrieval-Augmented Generation)**  
  Uses a small curated corpus of:
  - Role definitions and skill maps
  - Interview best practices
  - Resume and LinkedIn tips  

  Fetches relevant chunks and lets the LLM generate grounded answers.

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, minimal JavaScript  
- **Data:** In‑memory Python structures for now (JSON planned)  
- **AI (planned):** OpenAI / Claude / Gemini LLM APIs, LangChain / similar for RAG  
- **Env/Tools:** `pip`, virtualenv / venv, `requirements.txt`

---

## 📦 Setup & Run (Local)

```bash
git clone https://github.com/<your-username>/propath-career-ai.git
cd propath-career-ai

python -m venv venv
# Windows:
# venv\Scripts\activate
# Linux / macOS:
# source venv/bin/activate

pip install -r requirements.txt

flask run  # or: python app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## 🧪 Project Status

- [x] Flask app skeleton  
- [x] GPA Calculator (MVP)  
- [x] Skill Gap Analyzer (MVP)  
- [x] Salary Estimator (MVP)  
- [x] Static Interview Q&A prototype  
- [x] Static Project ideas prototype  
- [ ] LLM chat endpoint  
- [ ] RAG pipeline for grounded answers  

---

## 📈 Why this project

In 2026, many portfolios show only basic chatbots or static dashboards.  
ProPath is built as a **practical, end-to-end tool** that:

- Solves a real problem for **students and freshers**  
- Combines **deterministic tools** (GPA, salary, skill gap) with **LLM intelligence**  
- Will explore **RAG workflows** instead of only “prompt + answer” demos  

This makes it a strong flagship project for roles like **LLM Engineer, Prompt Engineer, and AI Engineer (Fresher)**.

---

## 📬 Contact

Built by **Roshani Kumari**  

- GitHub: [@roshaniprajapati1252-sys](https://github.com/roshaniprajapati1252-sys)  
- LinkedIn: [linkedin.com/in/roshaniprajapati](https://www.linkedin.com/in/roshaniprajapati)

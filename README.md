# 🤖 AI Recruiter – Semantic Candidate Ranking System

> **Making hiring smarter with AI, not just keywords.**

## 📌 Problem Statement

Traditional Applicant Tracking Systems (ATS) often rely on keyword matching. This means highly capable candidates can be overlooked simply because their resumes don't contain the exact words used in a job description.

This project aims to solve that problem by building an AI-powered recruiter that understands the **meaning** of both job descriptions and candidate profiles instead of matching keywords alone.

---

# 🚀 Solution

The system reads a job description and compares it with every candidate profile using semantic embeddings.

Instead of only checking whether a candidate has written "Python" or "Machine Learning", the model understands the overall context, skills, experience, and profile quality before ranking candidates.

The result is a shortlist that is more aligned with how an experienced recruiter evaluates applicants.

---

# ✨ Features

- 🔍 Semantic candidate matching using Sentence Transformers
- 🧠 Hybrid AI scoring
- 📊 Explainable recommendations
- 📈 Interactive Streamlit Dashboard
- 📥 Submission CSV generation
- ⚡ Fast and lightweight implementation

---

# 🏗️ Project Architecture

```
Job Description
        │
        ▼
Sentence Embedding
        │
        ▼
Candidate Embedding
        │
        ▼
Cosine Similarity
        │
        ▼
Hybrid Score
 ├── Semantic Match
 ├── Experience
 ├── Profile Completeness
 ├── Recruiter Signals
        │
        ▼
Rank Candidates
        │
        ▼
Generate Submission CSV
```

---

# 📂 Project Structure

```
AI-Recruiter/
│
├── app.py
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── sample_candidates.json
│   ├── candidates.jsonl
│   ├── job_description.docx
│   └── sample_submission.csv
│
├── modules/
│   ├── embeddings.py
│   ├── explainer.py
│   ├── final_score.py
│   ├── job_parser.py
│   ├── parser.py
│   └── scorer.py
│
└── outputs/
    └── submission.csv
```

---

# ⚙️ Tech Stack

- Python
- Sentence Transformers
- Streamlit
- Pandas
- NumPy
- Scikit-Learn

---

# 🧠 Hybrid Scoring Strategy

Instead of relying only on semantic similarity, the final ranking combines multiple signals.

| Component | Weight |
|-----------|--------|
| Semantic Similarity | 70% |
| Experience | 15% |
| Profile Completeness | 10% |
| Recruiter Response | 5% |

This creates a more balanced ranking that considers both technical fit and overall candidate quality.

---

# 📊 Dashboard

The Streamlit dashboard provides:

- Candidate rankings
- Hybrid scores
- Explainable recommendations
- Score visualization
- CSV download

---

# 📥 Output

The system generates the submission file in the required format:

```
candidate_id,rank,score,reasoning
```

Example:

```
candidate_id,rank,score,reasoning
CAND_000012,1,0.91,"Strong semantic match; 8 years experience; Highly complete profile"
```

---

# ▶️ Running the Project

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
streamlit run app.py
```

---

# 💡 Future Improvements

- Vector database integration (FAISS/Pinecone)
- LLM-powered recruiter explanations
- Skill-gap analysis
- Multi-job comparison
- Resume parsing from PDF
- Interview recommendation engine

---
## Key Highlights

- Uses semantic embeddings instead of keyword matching.
- Combines semantic similarity with experience and recruiter signals.
- Generates explainable candidate rankings.
- Produces the required submission CSV automatically.
- Includes an interactive Streamlit dashboard for recruiters.
  
---
# 👨‍💻 About This Project

This project was built as part of the **Data & AI Challenge** with the goal of demonstrating how semantic AI can improve candidate screening beyond traditional keyword matching.

The focus was on building a practical, explainable, and recruiter-friendly prototype that can be extended into a production-ready hiring assistant.

---
## Conclusion

This project demonstrates how semantic AI can improve candidate screening by understanding context instead of relying solely on keyword matching. By combining semantic embeddings with hybrid scoring and explainable recommendations, the system provides recruiters with a practical and transparent way to identify the most relevant candidates.

## Thank you!

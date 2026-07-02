import json
import os
import pandas as pd
import streamlit as st

from modules.parser import candidate_to_text
from modules.job_parser import load_job_description
from modules.embeddings import get_embedding
from modules.scorer import calculate_similarity
from modules.final_score import calculate_final_score
from modules.explainer import generate_reason

st.set_page_config(
    page_title="AI Recruiter",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Recruiter")
st.write("### Semantic AI Candidate Ranking System")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📊 AI Recruiter")

st.sidebar.success("✅ Semantic Search")
st.sidebar.success("✅ Hybrid Scoring")
st.sidebar.success("✅ Explainable AI")
st.sidebar.success("✅ CSV Export")

# ---------------- LOAD DATA ---------------- #

with open("data/sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

job_text = load_job_description("data/job_description.docx")
job_embedding = get_embedding(job_text)

# ---------------- TOP METRICS ---------------- #

col1, col2, col3 = st.columns(3)

col1.metric("Candidates", len(candidates))
col2.metric("Embedding Model", "MiniLM")
col3.metric("Ranking", "Hybrid AI")

# ---------------- RANK CANDIDATES ---------------- #

results = []

for candidate in candidates:

    candidate_text = candidate_to_text(candidate)

    candidate_embedding = get_embedding(candidate_text)

    semantic = calculate_similarity(
        job_embedding,
        candidate_embedding
    )

    scores = calculate_final_score(
        candidate,
        semantic
    )

    reasons = generate_reason(
        candidate,
        semantic
    )

    results.append({

        "Candidate ID": candidate["candidate_id"],

        "Name": candidate["profile"]["anonymized_name"],

        "Role": candidate["profile"]["current_title"],

        "Experience": candidate["profile"]["years_of_experience"],

        "Final Score": scores["final_score"],

        "Semantic": scores["semantic"],

        "Experience Score": scores["experience"],

        "Profile Score": scores["profile"],

        "Recruiter Score": scores["recruiter"],

        "Reason": "; ".join(reasons)

    })

# ---------------- DATAFRAME ---------------- #

df = pd.DataFrame(results)

df = df.sort_values(
    by="Final Score",
    ascending=False
).reset_index(drop=True)

# ---------------- SUBMISSION FILE ---------------- #

submission_df = pd.DataFrame({

    "candidate_id": df["Candidate ID"],

    "rank": range(1, len(df) + 1),

    "score": df["Final Score"],

    "reasoning": df["Reason"]

})

os.makedirs("outputs", exist_ok=True)

submission_df.to_csv(
    "outputs/submission.csv",
    index=False
)

# ---------------- DASHBOARD ---------------- #

st.metric(
    "Candidates Processed",
    len(df)
)

st.subheader("🏆 Top 10 Recommended Candidates")

top10 = df.head(10)

st.dataframe(
    top10,
    use_container_width=True
)

st.subheader("📈 Top 10 Candidate Scores")

st.bar_chart(
    top10.set_index("Name")["Final Score"]
)

# ---------------- DOWNLOAD ---------------- #

st.subheader("📥 Download Submission")

csv = submission_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Submission CSV",
    data=csv,
    file_name="submission.csv",
    mime="text/csv"
)

# ---------------- PREVIEW ---------------- #

st.subheader("📄 Submission Preview")

st.dataframe(
    submission_df.head(10),
    use_container_width=True
)
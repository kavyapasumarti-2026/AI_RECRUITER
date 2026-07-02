from modules.explainer import generate_reason
from modules.final_score import calculate_final_score
import json

from modules.parser import candidate_to_text
from modules.job_parser import load_job_description
from modules.embeddings import get_embedding
from modules.scorer import calculate_similarity

# Load candidates
candidates = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            candidates.append(json.loads(line))
print(len(candidates))
# Load Job
job_text = load_job_description("data/job_description.docx")

# Generate Job Embedding
job_embedding = get_embedding(job_text)

# First Candidate
candidate = candidates[0]

candidate_text = candidate_to_text(candidate)

candidate_embedding = get_embedding(candidate_text)

score = calculate_similarity(
    job_embedding,
    candidate_embedding
)

results = []

for candidate in candidates:

    candidate_text = candidate_to_text(candidate)

    candidate_embedding = get_embedding(candidate_text)
semantic_score = calculate_similarity(
    job_embedding,
    candidate_embedding
)

final_score = calculate_final_score(
    candidate,
    semantic_score
)
reasons = generate_reason(
    candidate,
    semantic_score
)

results.append({
    "candidate_id": candidate["candidate_id"],
    "name": candidate["profile"]["anonymized_name"],
    "title": candidate["profile"]["current_title"],
    "experience": candidate["profile"]["years_of_experience"],
    "score": final_score,
    "reasons": reasons
})

results = sorted(
    results,
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP 10 CANDIDATES\n")

for rank, candidate in enumerate(results[:10], start=1):

    print("=" * 60)

    print(f"Rank #{rank}")

    print(f"Candidate : {candidate['name']}")

    print(f"ID        : {candidate['candidate_id']}")

    print(f"Role      : {candidate['title']}")

    print(f"Score     : {candidate['score']:.4f}")

    print("\nWhy Recommended:")

    for reason in candidate["reasons"]:
        print(reason)

    print("=" * 60)
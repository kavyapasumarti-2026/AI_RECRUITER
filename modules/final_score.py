def calculate_final_score(candidate, semantic_score):
    """
    Combines semantic similarity with profile signals.
    """

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    # Experience Score (0-1)
    experience = profile.get("years_of_experience", 0)
    experience_score = min(experience / 10, 1)

    # Profile Completeness (0-1)
    profile_score = signals.get("profile_completeness_score", 0) / 100

    # Recruiter Response Rate (0-1)
    recruiter_score = signals.get("recruiter_response_rate", 0)

    # Open to Work Bonus
    open_to_work = 1 if signals.get("open_to_work_flag", False) else 0

    # Final Hybrid Score
    final = (
        0.70 * semantic_score +
        0.15 * experience_score +
        0.10 * profile_score +
        0.05 * recruiter_score +
        0.02 * open_to_work
    )

    return {
    "final_score": round(final,4),
    "semantic": round(semantic_score,4),
    "experience": round(experience_score,4),
    "profile": round(profile_score,4),
    "recruiter": round(recruiter_score,4)
}
def generate_reason(candidate, semantic_score):
    """
    Generate recruiter-friendly explanation.
    """

    reasons = []

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    # Experience
    years = profile.get("years_of_experience", 0)

    if years >= 5:
        reasons.append(f"✔ {years} years of relevant experience")

    # Skills
    skills = candidate.get("skills", [])

    top_skills = [skill["name"] for skill in skills[:5]]

    if top_skills:
        reasons.append(
            "✔ Strong skills in: " + ", ".join(top_skills)
        )

    # Open to work
    if signals.get("open_to_work_flag"):
        reasons.append("✔ Open to work")

    # Profile Completeness
    completeness = signals.get("profile_completeness_score", 0)

    if completeness > 80:
        reasons.append("✔ Highly complete profile")

    # Recruiter Response
    response = signals.get("recruiter_response_rate", 0)

    if response > 0.30:
        reasons.append("✔ Good recruiter response rate")

    # Semantic
    reasons.append(
        f"✔ Semantic Match Score: {semantic_score:.2f}"
    )

    return reasons
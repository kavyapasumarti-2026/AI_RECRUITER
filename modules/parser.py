def candidate_to_text(candidate):
    profile = candidate["profile"]

    # Basic Profile
    headline = profile.get("headline", "")
    summary = profile.get("summary", "")
    current_title = profile.get("current_title", "")
    years = profile.get("years_of_experience", "")

    # Skills
    skills = ", ".join(
        skill["name"]
        for skill in candidate.get("skills", [])
    )

    # Career History
    experience = ""

    for job in candidate.get("career_history", []):
        experience += f"""
        Company: {job.get("company","")}
        Role: {job.get("title","")}
        Description: {job.get("description","")}
        """

    # Education
    education = ""

    for edu in candidate.get("education", []):
        education += f"""
        {edu.get("degree","")} in
        {edu.get("field_of_study","")}
        from {edu.get("institution","")}
        """

    full_text = f"""
    Headline:
    {headline}

    Summary:
    {summary}

    Current Role:
    {current_title}

    Experience:
    {years} years

    Skills:
    {skills}

    Career:
    {experience}

    Education:
    {education}
    """

    return full_text
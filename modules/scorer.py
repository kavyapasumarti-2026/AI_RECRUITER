from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(job_embedding, candidate_embedding):
    """
    Returns a similarity score between 0 and 1.
    """

    score = cosine_similarity(
        [job_embedding],
        [candidate_embedding]
    )[0][0]

    return float(score)
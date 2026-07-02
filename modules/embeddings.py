from sentence_transformers import SentenceTransformer

print("Loading AI model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Model Loaded")


def get_embedding(text):
    return model.encode(
        text,
        normalize_embeddings=True
    )
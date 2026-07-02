from docx import Document


def load_job_description(path):
    """
    Reads a .docx file and returns all text.
    """

    doc = Document(path)

    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text)

    return "\n".join(text)
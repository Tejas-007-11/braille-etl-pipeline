# structure.py
import uuid

def structure_to_json(text, lang="en"):
    paragraphs = text.split('\n')
    return {
        "document_id": str(uuid.uuid4()),
        "language": lang,
        "paragraphs": [
            {"id": i, "text": para.strip()} for i, para in enumerate(paragraphs) if para.strip()
        ]
    }

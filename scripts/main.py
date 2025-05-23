# main.py
from scripts.extract import extract_text_from_image
from scripts.clean import clean_text
from scripts.structure import structure_to_json
from scripts.translate import translate_to_braille

if __name__ == '__main__':
    text = extract_text_from_image('data/input/sample1.jpg')
    cleaned = clean_text(text)
    structured = structure_to_json(cleaned, lang='en')
    braille = translate_to_braille(cleaned)

    # Save outputs
    with open('data/output/sample_structured.json', 'w') as f:
        import json
        json.dump(structured, f, indent=2)

    with open('data/output/sample_braille.txt', 'w') as f:
        f.write(braille)

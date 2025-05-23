# Braille ETL Data Pipeline (Flickdone Assessment)

## 🧩 Project Overview
This pipeline extracts unstructured English/Hindi content (images or plain text) and converts it into structured JSON and braille translations using Tesseract OCR and Liblouis.

## ⚙️ Pipeline Stages

1. **Extract**: OCR using Tesseract
2. **Clean**: Remove noise, normalize formatting
3. **Structure**: Convert to structured JSON with paragraph metadata
4. **Translate**: Use Liblouis for Braille output

## 🗂 Directory Structure
- `data/input/`: Raw scanned or text files
- `data/output/`: Cleaned and structured Braille and JSON
- `scripts/`: Python logic
- `main.py`: Entry point of pipeline

## 🧪 Sample Usage

```bash
python -m scripts.main
pip install -r requirements.txt

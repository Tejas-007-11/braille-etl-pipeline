# extract.py
from PIL import Image
import pytesseract
import requests
from bs4 import BeautifulSoup

def extract_text_from_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path))

def extract_text_from_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return '\n'.join(p.get_text() for p in soup.find_all('p'))

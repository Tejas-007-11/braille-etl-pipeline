# translate.py
import subprocess

def translate_to_braille(text, table='en-us-g2.ctb'):
    with open('temp.txt', 'w') as f:
        f.write(text)
    result = subprocess.run(['lou_translate', table, 'temp.txt'], capture_output=True, text=True)
    return result.stdout

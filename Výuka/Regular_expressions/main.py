import requests
import re
from os.path import join, realpath, dirname, exists

file_path = join(dirname(realpath(_file_)), "Othello.txt")

if not exists(file_path):
    resp = requests.get("https://www.gutenberg.org/cache/epub/2267/pg2267.txt")
    if resp.ok:
        with open(file_path, "x", encoding=resp.apparent_encoding) as file:
            file.write(resp.text)

with open(file_path, "r", encoding="utf-8") as file:
    book = file.read()
    sentences1 = re.findall(r'((?<=[.!?])\s+)', book)
    print(len(sentences1))
    sentences2 = re.findall(r'(?<!\b[A-Z][a-z])\.((?<=[.!?])\s+)', book)
    print(len(sentences2))
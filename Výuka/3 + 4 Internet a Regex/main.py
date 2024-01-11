import requests
import re


#response = requests.get("https://www.gutenberg.org/cache/epub/2267/pg2267.txt")
#file = open("Othello.txt", "w")
#file.write(response.text)

with open("Othello.txt", "r", encoding="utf-8") as file:
    book = file.read()
    sentence = re.findall(r'[A-Z0-9](\d|\w| )+(\.|\?|\!)', book)
    print(len(sentence))
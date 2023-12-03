soubor = open("input.txt", "r")
text = soubor.read()
substring = text.split(" ")

substring.reverse()

newstring = " ".join(substring)

novysoubour = open("output.txt", "w")
novysoubour.write(newstring)
novysoubour.close

print(newstring)
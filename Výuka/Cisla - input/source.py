from os.path import realpath, dirname, join

with open(join(dirname(realpath(__file__)), "2000.txt"),
            "r", encoding = "utf_8") as file:
    data = []
    for radek in file.read().split('\n'):
        data.append(radek)

for cislo1 in data:
    for cislo2 in data:
        if cislo1+cislo2 == 2020:
            print(cislo1, cislo2)

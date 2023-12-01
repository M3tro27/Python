soubor = open("input.txt", "r")
radky = soubor.readlines()



cisla = []
vysledek = 0

for radek in radky:
    radek = radek.replace("one", "o1ne")
    radek = radek.replace("two", "t2wo")
    radek = radek.replace("three", "th3ree")
    radek = radek.replace("four", "fo4ur")
    radek = radek.replace("five", "fi5ve")
    radek = radek.replace("six", "si6x")
    radek = radek.replace("seven", "se7en")
    radek = radek.replace("eight", "ei8ht")
    radek = radek.replace("nine", "ni9ne")
    print(radek)
    for znak in radek:
        if znak.isdigit():
            cisla.append(znak)
    if len(cisla) == 1:
        cislo = str(cisla[0]) + str(cisla[0])
        vysledek += int(cislo)
    else:
        cislo = str(cisla[0]) + str(cisla[-1])
        vysledek += int(cislo)
    cisla = []


print(vysledek)
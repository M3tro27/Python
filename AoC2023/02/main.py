soubor = open("input.txt", "r")
radky = soubor.readlines()

suma = 0
#input = "Game 1: 4 blue, 7 red, 5 green; 3 blue, 4 red, 16 green; 3 red, 11 green"
for input in radky:
    cislohry = input[5:input.find(":")]
    mozne = True

    hra = input[input.find(":")+2:]
    tahy = hra.split("; ")

    for tazeni in tahy:
        kostky = tazeni.split(", ")
        for kostka in kostky:
            rozdeleni = kostka.split(" ")
            if rozdeleni[1] == "red" and int(rozdeleni[0]) > 12 or \
                rozdeleni[1] == "green" and int(rozdeleni[0]) > 13 or \
                rozdeleni[1] == "blue" and int(rozdeleni[0]) > 14:
               
                mozne = False
                #print(cislohry + " " + rozdeleni[0] + " " + rozdeleni[1])
                break

        if not mozne:
            break


    if mozne == True:
        print(suma, cislohry)
        suma += int(cislohry)
        
print(suma)

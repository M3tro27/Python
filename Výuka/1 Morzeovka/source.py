soubor = open("kod.txt", "r")
radky = soubor.readlines()

veta = ''

while veta != "/exit":

    veta = input("Zadej vetu: ")
    vysledek = ''

    for x in veta.upper():    
        for radek in radky:
            if radek[0] == x:
                vysledek = vysledek + radek[2:len(radek)-1] + ' '
                
    print(vysledek)
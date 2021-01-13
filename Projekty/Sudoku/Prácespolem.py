from random import randint, shuffle
from Grafika import *
cislaSeznam = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0 # počítá počet řešní

def obtiznostNastav(self):
    print("V případě zájmu udělejte prosím výstřižek sudoku")
    obtiznost = int(input("Zadejte obtiznost (1-3): \n"))
    if (obtiznost > 3):
        print(f"Zvolili jste spatnou obtiznost")
    elif (obtiznost < 1):
        print(f"Zvolili jste spatnou obtiznost")
    return obtiznost

def konzole(bod):
    print("Sudoku bod Ready")
    for sloupec in range(0, 9):
        print(
            f"{bod[sloupec][0]} {bod[sloupec][1]} {bod[sloupec][2]} | {bod[sloupec][3]} {bod[sloupec][4]} {bod[sloupec][5]} | {bod[sloupec][6]} {bod[sloupec][7]} {bod[sloupec][8]}")
        if (sloupec % 3 == 2):
            print("_____________________")

def checkBod(bod):
    """Kontroluje výskyt prvku v řádku a sloupci"""
    for rad in range(0, 9):
        for slo in range(0, 9):
            if bod[rad][slo] == 0:
                return False
    return True


def praceBod(bod, varianta):
    """Tato funkce pracuje jako funkce k naplnění a funkce k řešení sudoku, je toho dosáhnut pomocí parametrů:
        bod - parametr který pracuje s listem"""
    global counter
    for i in range(0, 81):
        rad = i // 9 # klasické dělení
        slo = i % 9 # modulo, zbytek po dělení, takže postupně budou hodnoty 1,2,3
        if bod[rad][slo] == 0:
            shuffle(cislaSeznam) # míchá seznam, aby nedocházelo k 1234..
            for value in (cislaSeznam):
                if not (value in bod[rad]): #kontroluje jestli je v radku
                    # kontroluje, zdali jsou hodnoty v jednotlivých sloupcíh, místo výpisu po prvcích jsem zvolil tuhle kontrolu cyklem
                    if not value in (bod[n][slo] for n in range(0, 8)):
                        square = []
                        # kontroluje, v jakém čtverci se pohybujeme, pro kontrolu, jestli číslo již není použito
                        if rad < 3:
                            if slo < 3:
                                square = [bod[i][0:3] for i in range(0, 3)]
                            elif slo < 6:
                                square = [bod[i][3:6] for i in range(0, 3)]
                            else:
                                square = [bod[i][6:9] for i in range(0, 3)]
                        elif rad < 6:
                            if slo < 3:
                                square = [bod[i][0:3] for i in range(3, 6)]
                            elif slo < 6:
                                square = [bod[i][3:6] for i in range(3, 6)]
                            else:
                                square = [bod[i][6:9] for i in range(3, 6)]
                        else:
                            if slo < 3:
                                square = [bod[i][0:3] for i in range(6, 9)]
                            elif slo < 6:
                                square = [bod[i][3:6] for i in range(6, 9)]
                            else:
                                square = [bod[i][6:9] for i in range(6, 9)]
                        if not value in (square[0] + square[1] + square[2]):
                            #Samotné rozdělení variant, pro jednu funkci, která pracuje s bodem
                            if(varianta==1):
                                bod[rad][slo] = value
                                if checkBod(bod):
                                    counter += 1
                                    break
                                else:
                                    if praceBod(bod,varianta):
                                        return True
                            else:
                                bod[rad][slo] = value
                                if checkBod(bod):
                                    return True
                                else:
                                    if praceBod(bod,varianta):
                                        return True
            break
    bod[rad][slo] = 0

#Funkce, která po naplnění začně náhodně mazat hodnoty v políčku a zároveň kontroluje možný počet řešení, tedy, aby byla splněna podmínka
# jednoho řešení
def vymazBod(bod, obtiznost):
    # těžkopádné nastavení obtížnosti, závislé na volbě uživatele
    pokusy=20+obtiznost*10
    while pokusy > 0:
        # vybírám jednotlivá náhodná políčka
        rad = randint(0, 8)
        slo = randint(0, 8)
        while bod[rad][slo] == 0:
            rad = randint(0, 8)
            slo = randint(0, 8)
        backup = bod[rad][slo]
        bod[rad][slo] = 0
        copybod = []
        for r in range(0, 9):
            copybod.append([])
            for c in range(0, 9):
                copybod[r].append(bod[r][c])
        #Zde dochází ke kontrolej jednoho řešení
        praceBod(copybod,1)
        if counter != 1:
            pokusy -= 1
    myPen.getscreen().update()
# přidání mainu

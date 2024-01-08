import argparse

def Factorial(cislo):
    faktorial = 1

    while cislo != 0:
        faktorial = faktorial * cislo
        cislo = cislo - 1
    
    return faktorial

parser = argparse.ArgumentParser(description="Faktorial cisla")
parser.add_argument("cislo", type=int)
args = parser.parse_args()

faktorial = Factorial(args.cislo)
print(faktorial)

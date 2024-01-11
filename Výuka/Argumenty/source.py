import argparse

def Factorial(cislo):
    faktorial = 1

    while cislo != 0:
        faktorial = faktorial * cislo
        cislo = cislo - 1
    
    print(faktorial)

def Mocnina(cislo, exponent):
    print(pow(cislo, exponent))

parser = argparse.ArgumentParser(description="Operace")
parser.add_argument("-n", type=int)
parser.add_argument("-o", type=str)
parser.add_argument("-e", type=int, default=1)
args = parser.parse_args()



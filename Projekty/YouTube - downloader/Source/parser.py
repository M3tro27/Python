import argparse

def vlajky():  
	parser = argparse.ArgumentParser(description='Odkaz youtube videa')
	parser.add_argument('-o', metavar='odkaz', help='Zde zadejte odkaz')
	parser.add_argument('-r', metavar='rozliseni', help='Zde zadejte pozadovane rozliseni (napr. "360p", "480p"...) ', default='nezadano')
	parser.add_argument('-t', metavar='titulky', help='Pokud chcete stáhnout i tutlky zadejte "ano" ', default='ne')
	args = parser.parse_args()
	return(args)

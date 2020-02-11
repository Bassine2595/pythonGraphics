# Bassine Ndao, Isabella Forman
# LS6 Projet

from Parse import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nom_fichier")
args = parser.parse_args()
paire = parseFile(args.nom_fichier)
for draw_elem in paire[1]:
	paire[0][draw_elem].draw()

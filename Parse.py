# Bassine Ndao, Isabella Forman
# LS6 Projet

from GFigure import *
from Coord import *
import re

def parseGroupString(regle):
	a = regle.upper().strip()
	paire = a.split(":")
	if a == paire:
		raise NameError("La règle de dessin n'est pas correcte")
	return (paire[0], paire[1].strip())

def parseShapeList(chaine):
	newListe = []
	exp = re.compile(r"(\w+\[.+?\],?\s?)")
	mListe = exp.findall(chaine)
	if mListe != None:
		insideExp = re.compile(r"(\w+)\[(.+?)\],?\s?")
		for x in mListe:
			m = insideExp.match(x)
			if m != None and m.group(1) != None and m.group(2) != None:
				newListe.append((m.group(1), m.group(2)))
	return newListe

def createNewFig(nom, type, parametres, d):
	m=re.search(r"SIZE=(\d+)", parametres)
	if m == None:
		raise Exception("Pas de taille")

	m1=re.search(r"POS=\((\d+),(\d+)\)",parametres)
	if(m1 != None):
		c=Coord(int(m1.group(1)), int(m1.group(2)))
	else:
		c=Coord(0,0)
	return Circle(nom, c, m.group(1))

def createNewGroup(regle, d):
	liste = parseGroupString(regle)
	liste2 = parseShapeList(liste[1])
	newGroup = Group(liste[0])
	for x in liste2:
		newGroup.add(createNewFig(liste[0], x[0], x[1], d))
	d[liste[0]] = newGroup


def parseFile(fichier):
	groups = dict()
	drawlist = []
	with open(fichier, "r") as f:
		lines = f.readlines()
		for x in lines:
			a = x.rstrip()
			m = re.match(r"DRAW (.+)", a)
			if m == None:
				createNewGroup(a, groups)
			else:
				items = m.group(1).strip().split(",")
				for y in items:
					drawlist.append(y)
		return (groups, drawlist)








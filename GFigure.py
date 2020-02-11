# Bassine Ndao, Isabella Forman
# LS6 Projet

from Coord import *
from turtle import *

class GFig:
	def __init__(self, nom, coord):
		self.nom = nom
		self.coord = coord

	def __str__(self):
		return self.nom + " " + str(self.coord)

class Circle(GFig):
	def __init__(self, nom, coord, rayon):
		self.figure = GFig(nom, coord)
		self.rayon = rayon

	def __str__(self):
		return str(self.figure) + " rayon du cercle = " + str(self.rayon)

	def move(self, newCoord):
		self.figure.coord += newCoord

	def draw(self):
		self.figure.coord.moveto()
		penup()
		right(90)
		forward(int(self.rayon))
		left(90)
		pendown()
		# color(self.figure.color)
		circle(int(self.rayon))
		self.figure.coord.moveback()
		penup()
		goto(0, 0)
		pendown()

class Group(GFig):
	def __init__(self, nom):
		self.nom = nom
		self.liste = []

	def add(self,element):
		self.liste.append(element)

	def __str__(self) :
		strRep = ""
		for i in self.liste:
			strRep = strRep + str(i) + "\n"
		return strRep

	def move(self,coord):
		for i in self.liste:
			i.move(coord)

	def draw(self):
		for i in self.liste:
			i.draw()



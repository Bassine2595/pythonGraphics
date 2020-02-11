# Bassine Ndao, Isabella Forman
# LS6 Projet


from turtle import *
from math import *

class Coord:
  def __init__(self,rayon,theta):
    self._theta = theta%360 if rayon >= 0 else (theta+180)%360
    self._rayon = abs(rayon)
  def cartesian(self):
    (x,y)= ( self._rayon* cos(radians(self._theta)),
             self._rayon* sin(radians(self._theta)) )
    return(x,y)
  def __add__(self,other):
    (x1,y1) = self.cartesian()
    (x2,y2) = other.cartesian() 
    (x3,y3) = (x1+x2, y1+y2)
    rayon = sqrt(x3**2 + y3**2) #pythagore
    theta = degrees(atan(y3/x3)) if abs(x3)> 0 else self._theta+other._theta
    if x3 < 0: theta+=180 
    new = Coord(rayon, theta)
    return new

  def __iadd__(self,other):
    self = self + other
    return self

  def copy(self):
    return Coord(self._rayon,self._theta)

  def moveto(self):
    penup()
    left(self._theta)
    forward(self._rayon)
    pendown()

  def moveback(self):
    penup()
    back(self._rayon)
    right(self._theta)
    pendown()
  def __str__(self):
    return "angle " + str(self._theta) + " et rayon " + str(self._rayon)


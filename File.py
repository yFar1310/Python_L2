# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:51:15 2022

@author: Farehan Yahya
"""
from Pile import *
class File:
    
    def __init__(self):
        self.entree=Pile()
        self.sortie=Pile()
    def file_vide(self):
        return self.entree.pile_vide() and self.sortie.pile_vide()
    def enfiler(self,x):
        self.entree.empiler(x)
    def defiler(self):
        if self.entree.pile_vide():
            while not self.sortie.pile_vide():
                enfiler(self.entree,depiler(self.sortie))
        return self.entree.depiler()
    def __str__(self):
          lst=self.sortie._contenu.copy()
          lst.reverse()
          lst.extend(self.entree._contenu)
          return " ".join(map(str, lst))
p1=Pile()
p1.empiler(4)
p1.empiler(5)
p1.empiler(6)
print(p1)
print()
f1=File()
f1.enfiler(4)
f1.enfiler(5)
f1.enfiler(6)
print(f1)
f1.defiler()
print(f1)    
    
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:31:39 2022

@author: Farehan Yahya
"""

class Pile:
    
    def __init__(self):
        self._contenu=[]
    def pile_vide(self):
        return self._contenu==[]
    def empiler(self,x):
        self._contenu.append(x)
    def sommet(self):
            return self._contenu[-1]
    def depiler(self):
            return self._contenu.pop()
    def __str__(self):
            return " ".join(map(str,self._contenu))
            
P=Pile()
P.empiler(1)
P.empiler(2)


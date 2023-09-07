# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:37:17 2022

@author: Farehan Yahya
"""

class Liste:
    def __init__(self):
        self.premier = None
        self.queue = None
    def est_vide(self):
        return self.premier==None and self.queue==None
    def __str__(self):
        if self.est_vide():
            return []
        else:
            return str(self.premier)+" "+self.queue.__str__()
    def taille(self):
        if self.est_vide():
            return 0
        else:
            return 1+self.queue.taille()
        
        
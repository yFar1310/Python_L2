# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:37:17 2022

@author: Farehan Yahya
"""

class ABR:
    def __init__(self):
        self.valeur = None
        self.gauche = None
        self.droit = None
        
        
        
        
    def est_vide(self):
        return self.valeur==None and self.gauche==None and self.droit==None
    
    
    
    
    
    
    def place(self,e):
        if self.est_vide():
            self.valeur = e
            self.gauche = ABR()
            self.droit = ABR()
        else:
            if e<self.valeur: 
                self.gauche.place(e)
            if e>self.valeur:
                self.droit.place(e)
                
                
                
    def __str__(self):
        if self.est_vide():
            return ""
        else:
            return "["+str(self.valeur)+""+self.droit.__str__()+""+self.gauche.__str__()+"]"
        
        
        
        
    def ajouts(self, *args):
        for a in args:
            self.place(a)
    
    
    


    def copie(self):
        if self.est_vide():
            return ABR()
        else:
            A=ABR()
            A.valeur = self.valeur
            A.gauche=self.gauche.copie()
            A.droit=self.droit.copie()
        return A
    def feuille(self):
        if self.valeur!=None:
            if self.droit.est_vide() and self.gauche.est_vide():
              return True
            else:
              return False
          
    def nbNoeuds(self):
        if self.est_vide():
            return 0
        else:
             return 1+self.droit.nbNoeuds() + self.gauche.nbNoeuds()
                 
    def nbFeuilles(self):
        if self.est_vide():
            return 0
        else:
             if not self.feuille():
                 return self.gauche.nbFeuilles() + self.droit.nbFeuilles()
             else:
                 return 1
        
    def Hauteur(self):
        if self.est_vide():
            return 0
        elif self.feuille():
            return 1
        else:
             return max(1+self.droit.Hauteur(),1+self.gauche.Hauteur())
            
    def Equilibré(self):
        if self.est_vide():
            return True
        else:
            if abs(self.gauche.Hauteur()-self.droit.Hauteur())<=1 and self.gauche.Equilibré() and self.droit.Equilibré():
                return True
            else:
                return False
        
        
A1 = ABR()
A1.ajouts(6)
A2 = ABR()
A2.ajouts(5,2,8,6,4)
print(A1.feuille()) 
print(A2.nbNoeuds()) 
print(A2.nbFeuilles())  
print(A2.Hauteur())        
            
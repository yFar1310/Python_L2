# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:43:22 2022

@author: Farehan Yahya
"""

def casesvoisines(lab,i,j):
        L=[]
        if i>0:
            if lab[i-1][j]==1:
                L.append((i-1,j))
        if j>0:
            if lab[i][j-1]==1:
                L.append((i,j-1))
        if i<len(lab)-1:
            if lab[i+1][j]==1:
                L.append((i+1,j))
        if j<len(lab)-1:
            if lab[i][j+1]==1:
                L.append((i,j+1))
        return L
def parcours(lab):
    L=[]
    i=0
    j=0
    while not lab[i][j]==1:
        j+=1
        voisinage= casesvoisines(lab, i, j)
        if voisinage != [] :
            L.append(voisinage[0])
        else:
            L.pop()    
            case = L[-1]
            i, j = case[0], case[1]
    return L
    
        
    
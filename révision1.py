# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:16:44 2022

@author: Farehan Yahya
"""


def somme_chiffres(n):
    s=0
    while n!=0:
      s+=n%10
      n=n//10
    return s

print(somme_chiffres(121))

def est_premier(n):
    divisible =False
    for i in range(2,n-1):
            if n%i==0:
                divisible=True
    if divisible == True:
        print('Pas premier')
    else:
        print('Premier')
       
#est_premier(8)       


def Syracus(n):
    while n!=1:
         if n%2==0:
             n=n/2
             print(int(n))
         else:
             n=n*3+1
             print(int(n))
    return int(n)
#print(Syracus(13))
         
def exprap(x,n):
    r=1
    while n!=0:
        if n%2==1:
            r=r*x
        x*=x
        n//=2
    return r

#print(exprap(5,4))

L=[3,2,1,0]
def cherche(L,x):
    for i in range(len(L)):
        if L[i]==x:
            return i,True
    return False
         
print(cherche(L,1))            

def tri_selection(L):
   n=len(L)
   for i in range(n-1): #parcours des éléments de L, sauf le dernier
          imin=i
          for j in range(i+1,n): #recherche de l‘indice imin du min de L[i:]
            if L[j]<L[imin]:
                imin=j
                L[i],L[imin]=L[imin],L[i]
   return L
            
print(tri_selection(L))


def tri_comptage(L):
    
    k=max(L)
    C=[0]*(k+1)
    for i in range(len(L)):
      C[L[i]]+=1
      p=0
    for i in range(k+1):  
     for j in range(C[i]):
           L[p]=i
           p+=1
    return L

print(tri_comptage(L))

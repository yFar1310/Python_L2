# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:41:48 2022

@author: Farehan Yahya
"""
from collections import deque

def dist_bfs_it(G,s): 
    dist=[-1]*len(G)
    pred = [-1]*len(G)
    dist[s]=0
    grey=deque() 
    grey.append(s)
    while len(grey)>0:
        s=grey.popleft() 
        for v in G[s]: 
            if dist[v]==-1: 
                 dist[v]=dist[s]+1 
                 pred[v]=s
                 grey.append(v) 
    return pred

def pcc_bfs(pred,s,t):
    L=[t]
    while s!=t:
        L.append(pred[t])
        t = pred[t]
    return L[::-1]

G=[[1,4],[0,5,2,6],[3,6],[2,7],[0,5],[1,4],[1,2,7],[3,6]]

#print(dist_bfs_it(G,1))
#print(pcc_bfs(dist_bfs_it(G,0), 1,3 ))

def Bellman_Ford_pred(G,s):
 d={k: float('inf') for k in G}
 P={}
 d[s]=0 
 ok=True
 while ok:
     ok = False
     for k in G:
       for i in range(len(G[k])): 
           v, c = G[k][i]  
           if d[v]>d[k]+c: 
              d[v]=d[k]+c
              P[v]=k
              ok = True
     return d,P
 
           
      
def cases_voisines(p,i,j):
  L=[]
  if j>0:
      L.append((i,j-1))
  if i>0:
      L.append((i-1,j))
  if j<p-1:
      L.append((i,j+1))
  if i<p-1:
      L.append((i+1,j))
  return L
        
print(cases_voisines(3,1,2))

def fct(n):
    for i in range(n):
        for j in range(n):
            print("A")
            print("\n")
            
print(fct(5))
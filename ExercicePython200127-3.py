#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:21:28 2020

@author: ludodata
"""

from random import randrange

valeurs = [i for i in range(1, 11)]
couleurs = [i for i in range(1, 5)]

nbTours = 7
score = 0


paquet = [(v, c) for v in valeurs for c in couleurs]
main1, main2 = [], []

def piocher():
    for i in range(nbTours):
    
        x = paquet[randrange(len(paquet))]
    
        main1.append(x)
    
        paquet.remove(x)
    
        y = paquet[randrange(len(paquet))]
        main2.append(y)
        paquet.remove(y)
    
def plusGrandQue():
    global score
    for i in range(nbTours):
        if main1[i][0] > main2[i][0] or (main1[i][0] == main2[i][0] and  main1[i][1] > main2[i][1]):
            score += 1
            print("+1")
        else:
            score -= 1
            print("-1")
            
piocher()
plusGrandQue()
        
print("Vainqueur :" + ("joueur 1" if score > 0 else "joueur 2"))


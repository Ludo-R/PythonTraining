#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:24:26 2019

@author: ludodata
"""
import math

# Exercice 1
# 3x²-7x = 23
# Résoudre l'équation

a = 3
b = 7
c = -23

delta = b * b - 4 * a * c

print(delta)
# delta > 0

x1 = (- b - math.sqrt(delta)) / (2 * a)
x2 = (- b + math.sqrt(delta)) / (2 * a)

# On appelle la fuction .sqrt de la library math pour trouvé la racine carré de
# delta

print(x1)
print(x2)

# Exercice 2
# Trouver la forme irréductible de la somme 217 / 440 + 101 / 256 + 86 / 71

sommeIrreductible = 217 / 440 + 101 / 256 + 86 / 71

print(sommeIrreductible)

d = 440*256*71
m = (217*256*71) + (101*440*71) + (86*440*256)

pgcd = math.gcd(d,m)

# Trouver  le pgcd avec la fonction gcd

print(pgcd)

# Exercice 3 Trouver le volum d'un cone

rayon = float (input("Saisir un rayon :"))

hauteur = float (input("Saisir une hauteur:"))

volume = (math.pi * (rayon**2) * hauteur) / 3

# apelle de la fonction pi

print(volume)
             

#Parti 2


print("Menu:\n\n 1. Pair ou Impaire \n\n 2. Triangle rectangle ou non\n\n 3. Quitter")
choiceMenu = input()

# Ajout d'un menu repetable avec boucle While // non demandé par l'exercice //
# Pour l'exercice 4 et 5 

while choiceMenu == "1" or "2":
    
    if choiceMenu == "1":
# Exercice 4 Programme permettant de dire si un nombre est pair ou impair
        nombreEntre = int(input("entree un nombre\n\n"))
        if nombreEntre%2 == 0:
            print("Pair")
        else:
            print("Impaire\n")
        print("Menu:\n\n 1. Pair ou Impaire \n\n 2. Triangle rectangle ou non")
        choiceMenu = input()
        

            
    elif choiceMenu == "2":
# Exercice 5 Programme permettant de dire si un triangle est rectangle ou non
# Et retourné aussi l'hypothénuse du triangle
        a = float (input("Saisir le coté a de votre triangle:"))
        b = float (input("Saisir le coté b de votre triangle:"))
        c = float (input("Saisir le coté c de votre triangle:"))
        
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            print("C'est un triangle rectangle")
        else:
            print("ce n'est pas un triangle rectangle")
        
        if a > b and a > c:
            print("L'hypothenuse est A")
        elif b > a and b > c:
            print("L'hypothenuse est B")
        elif c > a and c > b:
            print("L'hypothenuse est C")
        else:
            print("il n'y a pas dhypothenuse\n")
        print("Menu:\n\n 1. Pair ou Impaire \n\n 2. Triangle rectangle ou non")
        choiceMenu = input()

    else: break

    
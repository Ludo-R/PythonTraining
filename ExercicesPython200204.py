#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:49:25 2020

@author: ludodata
"""

"""
Exercice 1.
Ecrire une fonction hascap(s) qui renvoie tout les mots de la chaîne
s commençant par une majuscule.
Pour ce faire utiliser la fonction ord() pour obtenir le code ASCII des lettres (Les lettres majuscule ont un code allant de 65 à 90).

"""
from re import findall, sub

def hascaps(x):
    print(findall('[A-Z][a-z]+', x))
                 
s = "Onze ans déjà que cela passe vite Vous "
s += "vous étiez servis simplement de vos armes la "
s += "mort n‘éblouit pas les yeux des partisans Vous "
s += "aviez vos portraits sur les murs de nos villes"

hascaps(s) 

def hascaps2(x):
    l1= []
    l2 = x.split()
    for i  in l2:
        if ord(i[0]) in range(65,91):
            l1.append(i)
    return print(l1)

hascaps2(s)

"""
Exercice 2.
Proposer une fonction inflation(s) qui va doubler la valeur de tout les nombre dans la chaine s. Exemple : « Le prix est de 27 euros » devient « Le prix est de 54 euros ».
Utiliser la fonction enumerate() pour lancer une boucle for (Taper dans Google « enumerate boucle for ».)

"""

def inflation(x):
    l = x.split()
    j = []
    for num in l:
        if num.isnumeric():         #On demande pour chaque élément de la liste split s'il est numérique
            v = int(num) * 2        #Si Oui on le transforme en int
            j.append(str(v))        #On l'ajoute a une nouvelle liste puis on le reconverti en str
        else: 
            j.append(num)           #S'ils sont pas nuémrique ont les ajoute directement
    k = " ".join(j)                 #On joint le tout
    print(k)
    

    
y = "Le prix est de 200 euros"

inflation(y)

"""
Exercice 3.
Proposer une fonction lignes qui à partir d’une long chaîne s (>100 caractères) renvoie une liste de chaîne de caractères contenant chacun 24 caractères maximum et terminant par un espace.

"""
def lignes(x):
    l = x.split()
    l2 = [""]
    for i in l:
        i += " "
        if len(l2[-1]) + len(i) <= 24:
            l2[-1] += i
        else:
            l2.append(i[-1])
    print(l2)

lignes(s)
"""
Exercice 4.
Proposer un programme qui renvoie la liste de tout les nombres (y compris décimaux et négatifs) d’une chaîne de caractères.
A tester sur la chaîne : « Les 2 maquereaux valent 6.50 euros ».
"""

def numList(x):
    motif = '[0-9]*(?:[\.\,]?[0-9]+)'
    print(findall(motif, x))
               
m = 'Les 2 maquereaux valent 6.50 euros'
numList(m)

"""
Exercice 5.
Proposer une fonction arrondi(s) qui dans la chaîne s troncature tout les nombre décimaux. On autorise les nombres négatifs.q
Pour ce faire, vous avez la possibilité d’utiliser :
des () pour désigner des blocs de données dans l’expression rationnelle. pour remplacer chacun des blocs l’expression est r’\1_\2_’.
    
"""
def arrondi(x):
    s1 = sub('\.[0-9]*', '', x)
    print(s1)

arrondi(m)
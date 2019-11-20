#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:36:21 2019

@author: ludodata
"""
# Création fonction isPalindrome // non demandé par l'exercice

def isPalindrome(x):
    y = []
    for i in x:
        y.insert(0, i)
    if x == y:
        print("c'est un palindrome(fonction)")
    else:
        print("Ce n'est pas un palindrom(fonction)")
        
def isPalindrome2(x):
    if x == x[::-1]:
        print("C'est un palindrome(fonction2)")
    else:
        print("Ce n'est pas un palindrome(fonction2)")

# Exercice 2 Ecrire un programme qui vérifie si la liste est un palindrome

list = [1, 2, 3 , 4 , 3, 2, 1]
listReverse = []

for i in list:
    listReverse.insert(0, i)
if list == listReverse:
    print("C'est un palindrome")
else: 
    print("ce n'est pas un palindrome")

# Non demandé par l'exercice 
#   Autre possibilité -> 
if list == list[::-1]:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")
    
# Test avec une chaine de caractère
chaine = "elle"

if chaine == chaine[::-1]:
    print(chaine + " est un palindrome(test variable chaine de caractere)")
else:
    print(chaine + " n'est pas un palindrome")

# Test des fonctions
    
isPalindrome(list)
isPalindrome2(list)
isPalindrome2("Bonjour")
isPalindrome2("elle")
        

# Exercice 1 Crée un programme qui calcule le prix TTC d'une saisie eet qui s
# s'arrrete que si l'utilisateur rentre 0.

prixHt = 1

while prixHt != 0:
    
    prixHt = float (input("Saissisezz votre prix Hors taxe:\n"))
    
    prixTtc = prixHt * 1.20
    print("\nLe prix TTC est de :\n")
    print(prixTtc)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:37:52 2020

@author: ludodata
"""



class formulaire:
    
    def __init__(self, nom, prenom, anneeNaissance):

        self.nom = nom.upper()
        self.prenom = prenom.upper()
        self.anneeNaissance = anneeNaissance
        
    def age(self):
        return 2020 - self.anneeNaissance
    def majeur(self):
        return self.age() >= 18
    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom
    def doublon(self, double):
        return self.nom == double.nom and self.prenom == double.prenom and self.anneeNaissance == double.anneeNaissance
    
    def __str__(self):
      return (self.nom + ", " + self.prenom + ", " + str(self.anneeNaissance))
    
def addList(y, x):    
    y.append(x)    

instance = []

jd = formulaire('Doe', 'John', 2005)
addList(instance, jd)

ad = formulaire('doe', 'Alice', 2000)
addList(instance, ad)

bd = formulaire('Doe', 'John', 2005)
addList(instance, bd)

cd = formulaire('Arr', 'orrr', 1999)
addList(instance, cd)

od = formulaire('zee', 'azz', 2019)
addList(instance, od)

a = sorted(instance, key=lambda formulaire: formulaire.anneeNaissance)
for i in a :
    print(i)

print(ad.majeur())
print(jd.memeFamille(ad))
print(jd.doublon(ad))
print(jd.doublon(bd))





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:57:52 2019

@author: ludodata
"""


import matplotlib.pyplot as plt
import pandas

#Import d'un fichier excel et création des colonees
df = pandas.read_excel('/Users/ludodata/Simplon/autompg.xlsx', sep = '\t', names = ['mpg', 'cylindre', 'deplacement', 'puissance', 'poids', 'acceleration', 'annee modele', 'origine', 'nom de la voiture'])

#création des deux variable, qui vont chercher deux élément dans la liste.
x = df['annee modele']
y = df['puissance']

#config du graphique qui va sortir dans la console
plt.figure(figsize=(10, 5))
plt.grid(True)
plt.xlabel("annee modele")
plt.ylabel("puissance")
plt.title("Graphique TEST")
plt.bar(x, y)



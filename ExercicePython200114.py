#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:59:38 2020

@author: ludodata
"""

# Appli requetage d'une base de données 

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://root:sqlpwd@localhost/opendata")

def menu():
    choiceMenu = input("Bonjour, Séléctionner votre choix :\n\n1. Connaitre le nombre d'entreprise existant sur marseille \n2. Nombre entreprise par arrondissement \n3. Nombre entreprise par secteur \n4. Nombre d'entreprise par secteur et arrondissement \n5. Nombre entreprise par année de création \n6. Quelle est la durée de vie moyeenne d'une entreprise à Marseille \n7. Evolution du nombre d'établissement ces 10 dernières années \n8. Ancienneté des établissement toujours ouvert \n9. Proportion des établissment selon leurs classification \n10. Quitter\n")

    if choiceMenu == "1":
        df = pd.read_sql_query('SELECT count(*) FROM testquery', engine)
        print(df)
        menu()
    elif choiceMenu == "2":    
        cpInput = input("Veuillez entrer un code Postal : ")
        df = pd.read_sql_query('SELECT count(*) as Resultat FROM testquery WHERE codePostalEtablissement = "%s"' % (cpInput), engine)
        print(df)
        menu()
    elif choiceMenu == "3":
        secteurInput = input("Veuillez entrer un secteur d'activité : ")
        df = pd.read_sql_query('SELECT count(*) as Resulat FROM testquery WHERE LIB_NAP600 = "%s"' % (secteurInput), engine)
        print(df)
        menu()
    elif choiceMenu == "4":
        secteurInput = input("Veuillez entrer un secteur d'activité : ")
        cpInput = input("Veuillez entrer un code postal : ")
        df = pd.read_sql_query('SELECT count(*) FROM testquery WHERE LIB_NAP600 = "%s" AND codePostalEtablissement = "%s"' % (secteurInput, cpInput), engine)
        print(df)
        menu()
    elif choiceMenu == "5":
        anneeInput = input("Veuillez entrer une année de création : ")
        df = pd.read_sql_query("SELECT count(*) FROM testquery WHERE year(dateCreationEtablissement) ='%s'" % (anneeInput), engine)
        print(df)
        menu()
    elif choiceMenu == "6":
        cpInput = input("Veuillez entrer un code postal: ")
        df = pd.read_sql_query('SELECT AVG(timestampdiff(year, datecreationetablissement, datefin)) AS ddvEtablissement FROM testquery4 WHERE changementEtatAdministratifEtablissement = "1" and etatAdministratifEtablissement = "F" and codepostaletablissement = "%s"' % (cpInput), engine)
        
        # SELECT AVG(year(datefin) - year(datecreationetablissement))
        # Fonctionne aussi, Moins précis ?
        
        print(df)
        menu() 
        
    elif choiceMenu == "7":
        menu()
        
    elif choiceMenu == "8":
        menu()
    elif choiceMenu == "9":
        menu()
    elif choiceMenu == "10":
        print("A bientot")
    else:
        print("Choix incorrect\n")
        menu()
menu()

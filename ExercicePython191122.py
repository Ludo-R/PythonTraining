#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:47:32 2019

@author: ludodata
"""

from sqlalchemy import create_engine
import pandas as pd
import pymysql
import matplotlib.pyplot as plt


engine = create_engine("mysql+pymysql://root:sqlpwd@localhost/simplon")

df = pd.read_sql_query('SELECT DISTINCT console, possesseur FROM jeux_video', engine)

x = df["console"]
y = df["possesseur"]

print(df)

plt.style.use('dark_background')
plt.figure(figsize=(20, 10))
plt.grid(True)
plt.xlabel("console",c="#3B9FB2")
plt.ylabel("possesseur", c="#3B9FB2")

plt.title("Graphique TEST")
plt.scatter(x,y,s=2500,c="#3B9FB2",marker="d")

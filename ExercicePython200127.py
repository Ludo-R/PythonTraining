#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:34:16 2020

@author: ludodata
"""

class superstring:
    def __init__(self, chaine):
        self.ch = chaine
    def ajoute(self, char):
        self.ch += char
    def insert (self, char , i):
        self.ch = self.ch[:i] + char + self.ch[i:]
    def capsdown(self):
        self.ch = self.ch.lower()
    def upper(self):
        self.ch = self.ch.upper()
    def tri(self):
        self.ch = self.ch.split()
        self.ch = "-".join(sorted(self.ch))
    def __str__(self):
        return "Type : Superstring, Content : " + self.ch
        
        
        
s1 = superstring('ecouter bien c est important')
s1.ajoute("!")
s1.insert("Trés ", 8)
s1.upper()

print(s1)

s2 = superstring('ecouter bien c est important')
s2.ajoute("!")
s2.insert("Trés ", 8)
s2.upper()
s2.tri()

print(s2)
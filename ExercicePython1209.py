"""
Gestion de fiche de contact avec
prenom, nom, naissance, couriel
"""

### Section class

import pickle

listContact = []

class CarnetAdr(object):
    pass

class FichAdr(object):
    """ Fiche d'un contact """
    #Ajout méthode
    def __init__(self, prenom=None, nomfami=None,
                datenaiss=None, courriel=None):
        """ Initialise les 4 attributs.
        le format de datenaiss est JJ/MM/AAAA"""
        
        self.prenom = prenom
        self.nomfami = nomfami
        self.datenaiss = datenaiss
        self.courriel = courriel
        
        
        
    def __repr__(self):
        """ Produit une chaine selon l'objet FichAdr
        fourni en argument self."""
        
        patron = "Prenom = '%s',"+\
            "Nom = '%s', "+\
            "Datenaiss = '%s',"+\
            "Courriel = '%s'\n"
        return patron%(self.prenom, self.nomfami,
                       self.datenaiss, self.courriel)
    
    def addList(self):
        global listContact
        listContact.append(self)
        
    
def readContact():   
    with open('data.txt', 'rb') as fichier:
        mon_depickler = pickle.unpickler(fichier)
        full_list = []
        while 1:
            try:
                full_list.apped(mon_depickler.load())
            except EOFError:
                break
    return full_list
    
def newContact():
    print:("Veuillez ajouter un contact :")
        
    a = input("Prenom :\n")
    b = input("Nom :\n")
    c = input("Date Naissance :\n")
    d = input("Couriel : \n")
        
    contact = FichAdr(a, b, c, d).addList()
    return contact

def main():
    userChoice = input("Bonjour voulez vous entré un nouveau contact ? y/n , Si vous voulez afficher la liste des contact, entrer e\n")
    
    if userChoice == "y":
        newContact()
        main()
    elif userChoice == "e": 
        print(listContact)
        main()
    elif userChoice == "n":
        print("Merci Aurevoir")
    else:
        print("Nous n'avons pas compris votre saisie")
        main()
    
        
### Section fonction

main()
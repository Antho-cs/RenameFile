import os
import re
import natsort # https://stackoverflow.com/questions/2545532/python-analog-of-phps-natsort-function-sort-a-list-using-a-natural-order-alg

# Saisie du chemin à renommer
chemin = input("Quelle est le chemin du dossier a renommer ?") + '\\'
print(chemin)
# Liste de l'ensemble des fichiers présent
listeFichiers = natsort.natsorted( os.listdir(chemin) )
# Natsorted permet un tri Naturel, permettant la gestion de la casse des fichiers 1/10/100..

numero = int(input("Numéro ?"))

def renommage(number,commande):
    # Base du renommage
    base = recupNomDossier(chemin)
    numS = recupNumSaison(chemin)
    if numS < 10:
        numS = "0" + str(numS)
    saison = "S" + str(numS)
    # Boucle sur l'ensemble des fichiers présent
    for fichiers in listeFichiers:
        # Split afin de récuperer l'extension de fichiers en second index
        nomFichSeparer = fichiers.split(".")
        # Ajoute un 0 si l'on est en dessous du numéro 10
        if number < 10:
            strNum = "0" + str(number)
        else:
            strNum = str(number)
        # Structure de renommage
        name_fichier = base + " - " + saison + "EP" + strNum
        print(fichiers + " devient -> " + name_fichier)

        if commande == "Y":
            os.rename(chemin + fichiers, chemin + name_fichier + "." + nomFichSeparer[-1])

        number += 1

def recupNomDossier(string):
    path = os.path.dirname(string)  # Récupere le chemin du dossier courant
    path2 = os.path.dirname(path)  # Récupere le chemin du dossier parent
    return os.path.basename(path2)  # Retourne le Nom du dossier parent

def recupNumSaison(string):
    path = os.path.dirname(string)  # Récupere le chemin du dossier courant
    ssDossier = os.path.basename(path)  # Récupere le Nom du dossier courant
    # Regex de suppression de tout caracteres non Digit
    return int(re.sub(r'\D', "", ssDossier))  # retourne le numéro de la saison concerné.

renommage(numero,"N")
saisie = input("Tout est OK ? Y/N")
if saisie == "Y":
    renommage(numero,saisie)
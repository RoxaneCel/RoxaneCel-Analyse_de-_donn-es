#coding:utf8

import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math

#Fonction pour ouvrir les fichiers
def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu
fichier_csv = "/Users/roxanecelestine/Géographie - université/Master/M1-Géographie/Semestre 1/Analyse de données/Séance 6/src/Data/island-index.csv"
iles = ouvrirUnFichier(fichier_csv)
print(iles.head())

#Isolation de la colonne "Surface (km²)
surfaces = iles["Surface (km²)"].astype(float).tolist()
surfaces += [
    85545323, 
    37856841,
    7768030,
    7605049
]
print(surfaces)

# Tri de la liste en ordre décroissant
    #Fonction pour trier par ordre décroissant les listes (îles et populations)
def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

surfaces_triees = ordreDecroissant(surfaces)
print("Nombre de surfaces: ", len(surfaces_triees))

#Visualisation de la loi rang-taille
rangs = list(range(1, len(surfaces_triees)+1))

plt.figure(figsize=(8,6))
plt.plot(rangs, surfaces_triees, marker='o')
plt.title("Loi rang-taille des îles et continents")
plt.xlabel("Rang")
plt.ylabel("Surface (km²)")
plt.grid(True)

#Création du dosier
dossier_images = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(dossier_images, exist_ok=True)

fichier_image = os.path.join(dossier_images, "loi_rang_taille.png")
plt.savefig(fichier_image, dpi=300)

plt.show()
print(f"Image sauvegardée ici : {fichier_image}")


    #Fonction pour convertir les données en données logarithmiques
def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

surfaces_log = conversionLog(surfaces_triees)
rangs_log = conversionLog(list(range(1, len(surfaces_triees)+1)))

plt.figure(figsize=(8, 6))
plt.plot(rangs_log, surfaces_log, marker='o')
plt.title("Loi rang-taille (axes logarithmiques)")
plt.xlabel("Log(Rang)")
plt.ylabel("Log(Surface)")
plt.grid(True)

#Création du dossier
dossier_images = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(dossier_images, exist_ok=True)

fichier_image_log = os.path.join(dossier_images, "loi_rang_taille_log.png")
plt.savefig(fichier_image_log, dpi=300)

plt.show()
print(f"Image log-log sauvegardée ici : {fichier_image_log}")

#Avec cette action, il est possible faire un test sur les rangs. 
#Grâce à cela, on peut metter en relation le rang et la taille au moyen de test de corrélation. 

#Question 9: Ouverture du fichier
etats = ouvrirUnFichier("/Users/roxanecelestine/Géographie - université/Master/M1-Géographie/Semestre 1/Analyse de données/Séance 6/src/Data/Le-Monde-HS-Etats-du-monde-2007-2025.csv")
print(etats.head())

#Question 10: Isolement des colonnes
colonnes = ["État", "Pop 2007", "Pop 2025", "Densité 2007", "Densité 2025"]
etats_selection = etats[colonnes]
print(etats_selection.head())


#Fonction pour trier par ordre décroissant les listes (îles et populations)
def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

#Fonction pour obtenir le classement des listes spécifiques aux populations
def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

#Question 11: Ordonner de manière décroissante les listes
liste_etats = list(etats['État'])
pop_2007_brute = list(etats['Pop 2007'])
pop_2025_brute = list(etats['Pop 2025'])
dens_2007_brute = list(etats['Densité 2007'])
dens_2025_brute = list(etats['Densité 2025'])

rangs_pop_2007 = ordrePopulation(pop_2007_brute, liste_etats)
rangs_pop_2025 = ordrePopulation(pop_2025_brute, liste_etats)
rangs_dens_2007 = ordrePopulation(dens_2007_brute, liste_etats)
rangs_dens_2025 = ordrePopulation(dens_2025_brute, liste_etats)


#Fonction pour obtenir l'ordre défini entre deux classements (listes spécifiques aux populations)
def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

#Question 12:Comparaison sur la population et la densité
comparaison_2007 = classementPays(rangs_pop_2007, rangs_pop_2025)
comparaison_2007.sort()
print("\n---Comparaison de la liste sur la population et la densité en 2007 ")
for i in range(15):
    print(comparaison_2007[i])


#Question 13:Isolation de colonnes sous forme de listes différentes avec une boucle
liste_finale_pop = []
liste_finale_dens = []

for ligne in comparaison_2007:
    liste_finale_pop.append(ligne[0])
    liste_finale_dens.append(ligne[1])


#Question 14: Calcul du coefficient de dorrélation des rangs et concordance des rangs
from scipy.stats import spearmanr, kendalltau
rho, p_val_s = spearmanr(liste_finale_pop, liste_finale_dens)
tau, p_val_k = kendalltau(liste_finale_pop, liste_finale_dens)

print("\n---Question 14 : Les résultats statistiques ---")
print(f"Coefficient de Spearman (Rho) : {rho: .4f}")
print(f"Coefficient de Kendall (Tau) : {tau: .4f}")


#Partie sur les îles
iles = pd.DataFrame(ouvrirUnFichier(fichier_csv))

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().






#Partie sur les populations des États du monde
#Source. Depuis 2007, tous les ans jusque 2025, M. Forriez a relevé l'intégralité du nombre d'habitants dans chaque États du monde proposé par un numéro hors-série du monde intitulé États du monde. Vous avez l'évolution de la population et de la densité par année.
monde = pd.DataFrame(ouvrirUnFichier("/Users/roxanecelestine/Géographie - université/Master/M1-Géographie/Semestre 1/Analyse de données/Séance 6/src/Data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().



#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import os
# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("data/resultats-elections-presidentielles-2022-1er-tour.csv", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier)

# Mettre dans un commentaire le numéro de la question
# Question 1
# ...
print(contenu)
data = pd.DataFrame(contenu)
len(contenu)
len(contenu.columns)
print(contenu)

print("\n--- Types des colonnes dans le DataFrame ---")
print(contenu.dtypes)
contenu.head(1)
contenu.head(5)
print(contenu)
print(contenu.head(1))

print("\n--- Nom des colonnes et première ligne ---")
print(contenu.head(1))
print("/n--- Nombre inscrits ---")
print("\n--- Nombre d'inscrits ---")
print(contenu.head(10))
print(contenu.columns)

nb_lignes = len(contenu)
nb_colonnes = len(contenu.columns)
print("Nombre de ligne:", nb_lignes)
print("Nombre de colonnes:", nb_colonnes)
types_colonnes = [] 
types_colonnes = ['str', 'str', 'int', 'float', 'float', 'float', 'float', 'float', 'bool', 'bool','bool']

for col in contenu.columns:
    dtype = contenu[col].dtype 
    col = 'Voix.11'
    if pd.api.types.is_integer_dtype(dtype):
        types_colonnes.append('int')
    elif pd.api.types.is_float_dtype(dtype):
        types_colonnes.append('float')
    elif pd.api.types.is_bool_dtype(dtype):
        types_colonnes.append('bool')
    else:
        types_colonnes.append('str')

print(contenu.dtypes)
print(contenu.columns)
print(contenu.head())  

#Question 9 : sélectionner les inscrits
inscrits = contenu ["Inscrits"]
print(inscrits)

#Question 10: somme totale des inscrits
total_inscrits = contenu ["Inscrits"].sum()
print("Total des inscrits:", total_inscrits)

somme_colonnes=[] 
for col in contenu.columns:
    if contenu[col].dtype in ["int64","float64"]:
        somme_colonnes.append(contenu[col].sum())
print(somme_colonnes)#boucles qu'avec les données quantitatives donc int64(sans décimales) et flot64(avec décimales)

for col in contenu.columns:
    if contenu[col].dtype in ["int64", "float64"]:
        print(col, ":", contenu[col].sum())#boucles plus lisibles 

#Question 11: diagrammes en barres du nombre d'inscrits et de votants pour chaque département
dossier="Diagrammes en barres"
if not os.path.exists(dossier):
    os.makedirs(dossier)

#for i in range(len(contenu)):
    dept= contenu.loc[i, "Libellé du département"]
    inscrits = contenu.loc[i, "Inscrits"]
    votants = contenu.loc[i, "Votants"]
    plt.figure(figsize=(6,4))
    plt.bar(["Inscrits", "Votants"], [inscrits, votants], color=['blue', 'red'])
    plt.title(f"(dept)")
    plt.ylabel("Nombre de personnes")
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig(f"{dept}.png")
    plt.close()

#Question 12: diagrammes circulaire avec les votes blancs, nuls, exprimés et l'abstention
#for i in range(len(contenu)):
    votes= contenu.loc[i, "Blancs"]
    votes = contenu.loc[i, "Nuls"]
    votes = contenu.loc[i, "Exprimés"]
    votes = contenu.loc[i, "Abstentions"]
    plt.figure(figsize=(6,4))
    plt.pie(["Blancs", "Nuls","Exprimés", "Abstentions"], color=['blue', 'red'])
    plt.title(f"(dept)")
    plt.ylabel("Nombre de personnes")
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig(f"{dept}.png")
    plt.close()

#Question 13: histogramme de la distribution des inscrits
inscrits = contenu["Inscrits"]
plt.figure(figsize=(8,6))
plt.hist(inscrits, bins=20, density=True, edgecolor ='black', color='purple')
plt.title("Distribution des inscrits par département")
plt.xlabel("Nombre d'inscrits")
plt.ylabel("Nombre de départements")
plt.savefig(f"{inscrits}.png")
plt.close()
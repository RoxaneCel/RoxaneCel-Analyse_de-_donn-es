#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Calcul de la moyenne pour chaque colonne
donnees = pd.DataFrame(ouvrirUnFichier("/Users/roxanecelestine/Géographie - université/Master/M1-Géographie/Semestre 1/Analyse de données/Séance 5/Data/Echantillonnage-100-Echantillons.csv"))
print("\nNombre total de lignes :", len(donnees))
print("Nom des colonnes :", list(donnees.columns))
print(donnees)

#Théorie de l'échantillonnage (intervalles de fluctuation)
#L'échantillonnage se base sur la répétitivité.
print("Résultat sur le calcul d'un intervalle de fluctuation")

moyennes = {}
for col in donnees.columns:
    moyenne_col = donnees[col].mean()
    moyenne_arrondie =round(moyenne_col)
    moyennes[col] = moyenne_arrondie
print("\nMoyenne arrondie:")
for opinion, valeur in moyennes.items():
    print(f"{opinion} : {valeur}")

#Somme des trois moyennes
somme_moyennes = sum(moyennes.values())
frequences_echantillon= {}

for opinion, valeur in moyennes.items():
    freq = valeur / somme_moyennes
    frequences_echantillon[opinion] = round(freq, 2)
print("\nFréquence moyennes (échantillons)")
for opinion, freq in frequences_echantillon.items():
    print(f"{opinion}:{freq}")

#Population mère
population_mere = {
    "Pour": 852,
    "Contre" : 911,
    "Sans opinion" : 422
}

total_pop = sum(population_mere.values())
frequences_population = {}

for opinion, valeur in population_mere.items():
    freq = valeur / total_pop
    frequences_population[opinion] = round(freq, 2)

print("\nFréquence de la population mère")

for opinion, freq in frequences_population.items():
    print(f"{opinion}:{freq}")

#Calcul de l'intervalle de fluctuation de chaque fréquence
n = 2185
zC = 1.96

frequences_population = {op: val / sum(population_mere.values())for op, val in population_mere.items()}
intervalles = {}

for opinion, f in frequences_population.items():
    erreur = zC * math.sqrt((f * (1-f)) /n)
    borne_inf = round(f -erreur, 3)
    borne_sup = round(f + erreur, 3)
    intervalles[opinion] = (borne_inf, borne_sup)

print("\nIntervalles de fluactuation à 95 %")
for opinion, (inf, sup) in intervalles.items():
    print(f"{opinion} : [{inf}, {sup}]")

#Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.
print("Résultat sur le calcul d'un intervalle de confiance")

#Calcul de la première ligne
premier_echantillon = donnees.iloc[0]
print(premier_echantillon)
valeurs = list(premier_echantillon)
total = sum(valeurs)
print(total)

#Calcul des fréquences
print("Résultat du calcul de la fréquence")
frequences_echantillon_1 = {}
for i, col in enumerate(donnees.columns):
    freq= valeurs[i] / total
    frequences_echantillon_1[col] = round(freq, 2)
for opinion, freq in frequences_echantillon_1.items():
    print(f"{opinion}:{freq}")

#Calcul de l'intervalle pour chaque opinion
zC = 1.96
n = total
intervalles_confiance = {}

for opinion, f in frequences_echantillon_1.items():
    erreur = zC * math.sqrt((f * (1 - f)) / n)
    borne_inf = round(f - erreur, 3)
    borne_sup = round(f + erreur, 3)
    intervalles_confiance[opinion] = (borne_inf, borne_sup)
print("Intervalle de confiance pour le premier échantillon")

for opinion, (inf, sup) in intervalles_confiance.items(): 
    print(f"{opinion} : [{inf}, {sup}]")

#Théorie de la décision (tests d'hypothèse)
#La décision se base sur la notion de risques alpha et bêta.
#Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Théorie de la décision")
print("Résultats du test de Shapiro-Wilks")

from scipy.stats import shapiro
data1 = pd.read_csv("/Users/roxanecelestine/Géographie - université/Master/M1-Géographie/Semestre 1/Analyse de données/Séance 5/Data/Loi-normale-Test-1.csv")
data2 = pd.read_csv("/Users/roxanecelestine/Géographie - université/Master/M1-Géographie/Semestre 1/Analyse de données/Séance 5/Data/Loi-normale-Test-2.csv")

serie1 = data1 ["Test"]
serie2 = data2 ["Test"]

#Test de Shapiro-Wilks
stat1, p1 = shapiro(serie1)
stat2, p2 = shapiro(serie2)
def interpretation_shapiro(p):
    if p > 0.05:
        return "Distribution normale (p > 0.05)"
    else:
        return "Distribution non normale (p < 0.05)"
print(f"Fichier 1 → p = {p1:.4f} → {interpretation_shapiro(p1)}")
print(f"Fichier 2 → p = {p2:.4f} → {interpretation_shapiro(p2)}")

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,4))

#Pour le premier fichier
plt.subplot(1, 2, 1) 
sns.histplot(serie1, kde=True, color='skyblue', bins=30)
plt.title("Fichier 1 - Loi normale ?")
plt.xlabel("Valeurs")
plt.ylabel("Effectifs")

#Pour le second fichier
plt.subplot(1, 2, 2)
sns.histplot(serie2, kde=True, color='salmon', bins=30)
plt.title("Fichier 2 - Loi normale ?")
plt.xlabel("Valeurs")
plt.ylabel("Effectifs")

plt.tight_layout()
plt.savefig(f"img/loi_normale.png")
plt.show()


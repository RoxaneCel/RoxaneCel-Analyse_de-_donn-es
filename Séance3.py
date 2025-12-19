#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023

df = pd.read_csv("data/resultats-elections-presidentielles-2022-1er-tour.csv")

print (df.head())
print (df.columns)

#Question 5
quant = df.select_dtypes(include=["int64","float64"])
print(quant.head())

import numpy as np
moyennes = quant.mean().round(2).tolist()
print ("Moyennes:", moyennes)

medianes = quant.median().round(2).tolist()
print("Médianes :", medianes)

modes = quant.mode().iloc[0].round(2).tolist
print("Modes:", modes)

ecarts_type = quant.std().round(2).tolist()
print("Écarts-types:", ecarts_type)

ecarts_abs = (quant - quant.mean()).abs().mean().round(2).tolist()
print("Écarts absolus à la moyenne:", ecarts_abs)

etendues = (quant.max() - quant.min()).round(2).tolist()
print("Étendues:", etendues)


# Question 7
#Calcul des quartiles
Q1 = quant.quantile(0.25)
Q3 = quant.quantile(0.75)

#Distance interquartile
DIQ = (Q3 - Q1).round(2)
print("Distance interquartile :\n", DIQ)

#Calcul des déciles
D1 = quant.quantile(0.1)
D9 = quant.quantile(0.9)

#Distance interdécile
DID = (D9 - D1).round(2)
print("Distance interdécile :\n", DID)

# Question 8
import matplotlib.pyplot as plt

for col in quant.columns:
    plt.figure(figsize=(6, 4))  # taille de la figure
    plt.boxplot(quant[col])
    plt.title(f"Boîte à moustache de {col}")
    plt.ylabel(col)
    

    plt.savefig(f"img/boxplot_{col}.png")
    plt.close()  

# Question 9 et 10

import pandas as pd
islands = pd.read_csv("data/island-index.csv")

islands.columns = islands.columns.str.strip().str.replace("²", "2").str.replace(" ", "_")

surface_col = [col for col in islands.columns if "Surface" in col][0]
print(f"Colonne Surface utilisée : {surface_col}")

bins = [0, 10, 25, 50, 100, 2500, 5000, 10000, float('inf')]
labels = ["0-10", "10-25", "25-50", "50-100", "100-2500", "2500-5000", "5000-10000", ">=10000"]

# 5️⃣ Catégoriser la colonne Surface
islands["Surface_cat"] = pd.cut(
    islands[surface_col],
    bins=[0, 10, 25, 50, 100, 2500, 5000, 10000, float('inf')],
    labels=["0-10", "10-25", "25-50", "50-100", "100-2500", "2500-5000", "5000-10000", ">=10000"],
    right=True
)

counts = islands["Surface_cat"].value_counts().sort_index()
print("\nNombre d'îles par catégorie de surface :")
print(counts),
right=True


counts = islands["Surface_cat"].value_counts().sort_index()
print("\nNombre d'îles par catégorie de surface :")
print(counts)




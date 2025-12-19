#coding:utf8

import pandas as pd
import scipy
import scipy.stats as stats 
import numpy as np

#https://docs.scipy.org/doc/scipy/reference/stats.html

dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']
#print(dist_names)

#Distributions statistqiues de variables discrètes
#Loi de Dirac
valeur_dirac = 5 
echantillon_dirac = np.full(10, valeur_dirac)
print("Loi de Dirac:", echantillon_dirac)

#Loi uniforme discrète
echantillon_uniforme_discret = stats.randint.rvs(1, 7, size=10)
print("Loi uniforme discrète", echantillon_uniforme_discret)

#Loi binomiale
echantillon_binomiale = stats.binom.rvs(n=15, p=0.6, size=10)
print("Loi binomiale", echantillon_binomiale)

#Loi de Poisson
echantillon_poisson = stats.poisson.rvs(mu=5, size=10)
print("Loi binomiale", echantillon_poisson)

#loi de Zipf-Mandelbrot
echantillon_zipf = stats.zipf.rvs(a=4, size=10)
print("Loi de Zipf-Mandelbrot", echantillon_zipf)

#Distributions statistiques de varaibles continues 
#Loi de Poisson
echantillon_poisson = stats.poisson.rvs(mu=5, size=1000)
print("Loi du Poisson", echantillon_poisson)

#Loi normale
echantillon_normale = stats.norm.rvs(loc=0, scale=1, size=1000)
print("Loi normale", echantillon_normale)

#Loi log-normale
echantillon_lognormale = stats.lognorm.rvs(s=0.5, size=1000)
print("Loi lognormale", echantillon_lognormale)

#Loi uniforme
echantillon_uniforme = stats.uniform.rvs(0, 1, size=1000)
print("Loi Uniforme", echantillon_uniforme[:10])

#Loi du chi2
echantillon_chi2 = stats.chi2.rvs(df=3, size=1000)
print("Loi X²", echantillon_chi2[:10])

#Loi de Pareto
echantillon_pareto = stats.pareto.rvs(b=3, size=1000)
print("Loi de Pareto", echantillon_pareto[:10])

#Fonctions informatiques pour calculer la moyenne et l'écart-type des distributions précédentes
def ma_moyenne(data):
    return sum(data) / len(data)

def mon_ecart_type(data):
    m = ma_moyenne(data)
    variance = sum((x-m)**2 for x in data) /len(data)
    return variance ** 0.5

distributions = {
    "Poisson": echantillon_poisson,
    "Normale": echantillon_normale,
    "Log-normale": echantillon_lognormale,
    "X²": echantillon_chi2,
    "Uniforme": echantillon_uniforme,
    "Pareto": echantillon_pareto,
    "Dirac": echantillon_dirac,
    "Uniforme discrète": echantillon_uniforme_discret,
    "Binomiale": echantillon_binomiale,
    "Zipf-Mandelbrot": echantillon_zipf}
for nom, data in distributions.items():
    moyenne_calculee = ma_moyenne(data)
    ecart_calcule = mon_ecart_type(data)
    print(f"{nom}: moyenne = {moyenne_calculee: .3f}, écart-type = {ecart_calcule: .3f}")
    
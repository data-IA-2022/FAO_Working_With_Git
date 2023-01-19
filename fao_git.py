import numpy as np
import pandas as pd
import sqlite3
from glob import glob
from os import chdir, path

def grp1(dir):
    #Group 1, réponse à la question X : calcul...
    print("Résultat Q1:...")
def grp2(dir):
    df_population = pd.read_csv(dir+'/FAOSTAT_2013_population.csv')
    # On retire la Chine qui est en doublon
    df_population.query('Country != "China"', inplace=True)
    poptot = df_population['population'].sum() * 1000
    print(f"Résultat Q2: {poptot}")
def grp3(dir):
    #Group 3, réponse à la question X : calcul...
    print("Résultat Q3:...")

def grp4(dir):
    #Group 4, réponse à la question X : calcul...
    print("Résultat Q4:...")

def grp5(dir):
    #Group 5, réponse à la question X : calcul...
    print("Résultat Q5:...")

def grp6(dir):
    #Group 6, réponse à la question X : calcul...
    print("Résultat Q6:...")

def grp7(dir):
    #Group 7, réponse à la question X : calcul...
    print("Résultat Q7:...")


#..................................

print("Projet commun")
dir='fao_2013'
grp1('dir')

#importation des librairies python
import os
import pandas as pd
import glob
import itertools
import numpy as np
import platform
platform.system()
csv_path = f'{str(os.getcwd())}/fao_2013'
if str(platform.system()) == 'Windows':
    csv_path.replace('/','\\')
else:
    csv_path
# Récupération des chemin vers les fichiers csv

def find_csv_filenames(path_to_dir=os.getcwd(), extension="csv"):
    filenames = []
    for name in glob.glob(f'{path_to_dir}/*.{extension}'):
        filenames.append(name)
    return filenames
all_csv_files= find_csv_filenames(path_to_dir=csv_path)
# print(all_csv_files)

# Création d'un dictionaire avec nom des fichiers csv comme Key et dataframe comme value

col_names= ['Code Domaine', 'Domaine', 'Code Pays', 'Pays', 'Code Élément',
            'Élément', 'Code Produit', 'Produit', 'Code année', 'Année', 'Unité',
            'Valeur', 'Symbole', 'Description du Symbole']
df_dict = {}
for f in all_csv_files:
    df_name= f.split("/")[-1].replace(".csv", "").split("_")[-1]
    if "FAOSTAT_2013" in f:
        df_dict[f'{df_name}'] = pd.read_csv(f, encoding='utf-8', quotechar='"', delimiter=',', names= col_names, header=0)
    else:
        df_dict[f'{df_name}'] = pd.read_csv(f, encoding='utf-8', quotechar='"', delimiter=',')

# print(df_dict.keys())


# Définition des Dataframes

animal= df_dict["animal"]
cereal= df_dict["cereal"]
population= df_dict["population"]
alimentation= df_dict["alimentation"]
vegetal= df_dict["vegetal"]
# area= df_dict["area"]

# Définir les codes pays comme index des Df
animal.index= animal["Code Pays"]
animal.index.name= "Code_Pays_id"
cereal.index= cereal["Code Pays"]
cereal.index.name= "Code_Pays_id"
population.index= population["Code Pays"]
population.index.name= "Code_Pays_id"
# Masque pour supprimer les autres valeurs de chine
alimentation = alimentation[~alimentation['Pays'].isin(['Chine - RAS de Hong-Kong','Chine - RAS de Macao', 'Chine, continentale', 'Chine, Taiwan Province de'])]

alimentation.index= alimentation["Code Pays"]
alimentation.index.name= "Code_Pays_id"

vegetal.index= vegetal["Code Pays"]
vegetal.index.name= "Code_Pays_id"

# nb lignes et nb colonnes de nos df
# print(animal.shape)
# print(cereal.shape)
# print(population.shape)
# print(alimentation.shape)
# print(vegetal.shape)


# ma réponse à la question 1
def grp1(dir):
    #Group 1, réponse à la question X : calcul...
    # Nombre d'humain sur la planète
    #sum of value in population
    pop_total = population['Valeur'].sum()
    print(f'Il y avait {(pop_total*1000):,} habitants sur la planète en 2013'.replace(',', ' '))

def grp2(dir):
    #Group 2, réponse à la question X : calcul...
    print("Résultat Q2:...")
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
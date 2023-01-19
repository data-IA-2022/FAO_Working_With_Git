import pandas as pd

def grp1(dir):
    #Group 1, réponse à la question X : calcul...
    print("Résultat Q1:...")
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

def question_6(aliments_df):
    #Group 6, réponse à la question X : calcul...
    print("Résultat Q6:...")

    aliments_df.drop(aliments_df[aliments_df['Pays'] == 'Chine'].index, inplace=True)
    aliments_df["dispo_interieure_alimentaire_kg"] = aliments_df["Disponibilité intérieure"]*1000000
    aliments_df["dispo_interieure_alimentaire_kcal"] = aliments_df["dispo_interieure_alimentaire_kg"]*aliments_df["ratio_kcal/kg"]
    dispo_mondiale_vegetaux_df = aliments_df[aliments_df['Origine'] == 'Végétale']
    dispo_mondiale_vegetaux_df[['Pays', 'Origine', 'Produit', 'dispo_interieure_alimentaire_kcal']]
    dispo_mondiale_vegetaux_df_sum = dispo_mondiale_vegetaux_df[['dispo_interieure_alimentaire_kcal']].sum()
    dispo_mondiale_vegetaux_df_sum
    print(dispo_mondiale_vegetaux_df_sum)

question_6(aliments_df)
def grp7(dir):
    #Group 7, réponse à la question X : calcul...
    print("Résultat Q7:...")

#..................................
def grpMaud_Lorenzo(dir):
    #Group 7, réponse à la question X : calcul...
    print("Résultat Q7:...")



print("Projet commun")
dir='fao_2013'
grp1(dir)
lorenzo(dir)
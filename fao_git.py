import pandas as pd
#trolol23
#pouet
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

def grp6(dir):
    #Group 6, réponse à la question X : calcul...
    print("Résultat Q6:...")

def grp7(dir):
    #Group 7, réponse à la question X : calcul...
    #--------------------------------- Nombre d'humains sur la planète (question 1)------------------------------------
    import os
    import glob
    from colorama import Fore, Back, Style
    #----------------------------- Récupération des fichier dans un dataframe -----------------------------------------
    fns=glob.glob('fao_2013/*.csv', recursive=True)

    df_bigTab = pd.DataFrame(columns=['Code Domaine', 'Domaine', 'Code Pays', 'Pays', 'Code Élément',
        'Élément', 'Code Produit', 'Produit', 'Code Année', 'Année', 'Unité',
        'Valeur', 'Symbole', 'Description du Symbole'])


    nameModificateur=['Code Domaine', 'Domaine', 'Code Pays', 'Pays', 'Code Élément',
        'Élément', 'Code Produit', 'Produit', 'Code Année', 'Année', 'Unité',
        'Valeur', 'Symbole', 'Description du Symbole']
    #-------------------------- Construction du big Tableau avec tous les fichiers-------------------------------------
    for fn in fns:
        fns = fn[13:-4]
        df=pd.read_csv(fn, names=nameModificateur, header=0)
        print("\n")  
        print(f"{Fore.YELLOW}---------------------- Récupération du fichier {fns} --------------------{Style.RESET_ALL}\n")
        print(f"- {fn:50s} ({df.shape[0]:6d}, {df.shape[1]:2d}) - {Fore.BLACK}{Back.CYAN}{fns}{Style.RESET_ALL} \n")
        print(f"{Fore.YELLOW}------------------------------------------------------------------------------{Style.RESET_ALL}\n")
        print("\n")
        print(f"{Fore.YELLOW}------------------------ Analyse du fichier {fns} ------------------------{Style.RESET_ALL}\n")
        print(f"{df.describe()}")
        print("\n")
        print(f"{Fore.YELLOW}-------------------------------------------------------------------------------{Style.RESET_ALL}\n")
        df_bigTab=df_bigTab.append(df)
    pop_planetaire = df_pop['Valeur'].sum()
    print (f"La population mondiale en 2013 est de : {pop_planetaire}")
    df_pop = df_pop.loc[df_pop["Pays"] != "China"]
    pop_planetaire = df_pop['Valeur'].sum()
    print (f"La population mondiale en 2013 est de : {pop_planetaire}")


#..................................

print("Projet commun")
dir='fao_2013'
grp1('dir')
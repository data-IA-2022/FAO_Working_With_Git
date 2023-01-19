import pandas as pd


def grp1(dir):
    dir = "fao_2013/FAOSTAT_2013_population.csv"
    #Group 1, réponse à la question X : calcul...
    print("Résultat Q1:...")
    #chemin du fichier population qui est dans le meme dossier 
    #lecture du fichier csv
    df_pop = pd.read_csv(dir)
    #print(df_pop)
    #isolation de la collone d'intérêt
    df_popVal = df_pop[['Value']]
    #calcul de la somme des populations des pays du fichier
    df_popSum = df_popVal.sum()*1000 # *1000 car unité est par miller d'individus
    #print(df_popSum)
    # somme des populations est de 8413993000 ... en 2013 ce qui semble élevé
    #drop Chine car plusieurs référence
    df_pop_update = df_pop.drop(df_pop[(df_pop['Country Code']) & (df_pop['Country'] == 'China')].index, inplace=True)
    #isolation de la collone d'intérêt
    df_popVal2 = df_pop[['Value']]
    #calcul de la somme des populations des pays du fichier
    df_popSum = df_popVal2.sum()*1000 # *1000 car unité est par miller d'individus
    print(df_popSum) 

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
class exercice_6:
    def __init__(self):
        import pandas as pd
        animals_df = pd.read_csv('https://raw.githubusercontent.com/Lorenzo1208/Brief_fao/main/FAOSTAT_2013_animal.csv')
        animals_df.rename(columns={'Code Domaine':'Code_Domaine', 'Code Pays': 'Code_Pays','Code Élément	':'Code_Élément', 'Code Produit': 'Code_Produit', 'Valeur': 'quantité',  'Code Année':'Code_Année', 'Description du Symbole': 'Description_du_Symbole'}, inplace=True)
        vegetal_df = pd.read_csv('https://raw.githubusercontent.com/Lorenzo1208/Brief_fao/main/FAOSTAT_2013_vegetal.csv')
        vegetal_df.rename(columns={'Code Domaine':'Code_Domaine', 'Code Pays': 'Code_Pays','Code Élément':'Code_Élément', 'Code Produit': 'Code_Produit', 'Code Année':'Code_Année','Valeur':'quantité', 'Description du Symbole': 'Description_du_Symbole'}, inplace=True)
        animals_df['Origine'] = 'Animale'
        vegetal_df['Origine'] = 'Végétale'
        aliments_df = pd.concat([animals_df,vegetal_df])
        aliments_df = aliments_df.pivot_table(
            index=["Code_Pays","Pays","Code_Produit","Produit", "Origine"],
            columns = ["Élément"], values=["quantité"], aggfunc=sum)

    def réponse_6(self):
        print("dispo_interieure_alimentaire_kcal = Disponibilité intérieure * 1000000 * ratio_kcal/kg")

obj = exercice_6()
obj.réponse_6()
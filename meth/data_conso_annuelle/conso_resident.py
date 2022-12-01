import pandas as pd
import numpy as np

cons_total = "Consommation annuelle totale de l'adresse (MWh)"
cons_moyen = "Consommation annuelle moyenne par logement de l'adresse (MWh)"
cons_commune = "Consommation annuelle moyenne de la commune (MWh)"


# Donnée par année
df_2018 = pd.read_csv("./data_conso_annuelle/consommation-annuelle-residentielle-par-adresse2018.csv", sep=';')
df_2019 = pd.read_csv("./data_conso_annuelle/consommation-annuelle-residentielle-par-adresse2019.csv", sep=';')
df_2020 = pd.read_csv("./data_conso_annuelle/consommation-annuelle-residentielle-par-adresse2020.csv", sep=';')
df_2021 = pd.read_csv("./data_conso_annuelle/consommation-annuelle-residentielle-par-adresse2021.csv", sep=';')

# Nettoyage des données (déja fait dans les .csv du github)
#df_2018 = df_2018.drop(['Code IRIS', 'Numéro de voie', 'Indice de répétition',
#                       'Type de voie', 'Libellé de voie', 'Segment de client',
#                        'Tri des adresses','Année','Nom IRIS'], axis=1)
#
#df_2019 = df_2019.drop(['Code IRIS', 'Numéro de voie', 'Indice de répétition',
#                       'Type de voie', 'Libellé de voie', 'Segment de client',
#                        'Tri des adresses','Année','Nom IRIS'], axis=1)
#
#df_2020 = df_2020.drop(['Code IRIS', 'Numéro de voie', 'Indice de répétition',
#                       'Type de voie', 'Libellé de voie', 'Segment de client',
#                        'Tri des adresses','Année','Nom IRIS'], axis=1)
#
#df_2021 = df_2021.drop(['Code IRIS', 'Numéro de voie', 'Indice de répétition',
#                       'Type de voie', 'Libellé de voie', 'Segment de client',
#                        'Tri des adresses','Année','Nom IRIS'], axis=1)


# Création département
df_2018['Departement'] = df_2018['Code INSEE de la commune']
df_2019['Departement'] = df_2019['Code INSEE de la commune']
df_2020['Departement'] = df_2020['Code INSEE de la commune']
df_2021['Departement'] = df_2021['Code INSEE de la commune']
#df['Departement'] = df['Departement'].apply(get_2_digit)
df_2018['Departement'] = df_2018['Departement'].apply(
    lambda x: (x//10**4 % 10)*10 + (x//10**3 % 10))
df_2019['Departement'] = df_2019['Departement'].apply(
    lambda x: (x//10**4 % 10)*10 + (x//10**3 % 10))
df_2020['Departement'] = df_2020['Departement'].apply(
    lambda x: (x//10**4 % 10)*10 + (x//10**3 % 10))
df_2021['Departement'] = df_2021['Departement'].apply(
    lambda x: (x//10**4 % 10)*10 + (x//10**3 % 10))
    

# Commune qui consomme le plus dans l'année:
df_max = df_2018[cons_commune].max()
df_max_ville_2018 = df_2018[df_2018[cons_commune] == df_max]
df_max_ville_2018 = df_max_ville_2018['Nom de la commune'].unique().tolist()
df_max_ville_2018.append(df_max)

df_max = df_2019[cons_commune].max()
df_max_ville_2019 = df_2019[df_2019[cons_commune] == df_max]
df_max_ville_2019 = df_max_ville_2019['Nom de la commune'].unique().tolist()
df_max_ville_2019.append(df_max)

df_max = df_2020[cons_commune].max()
df_max_ville_2020 = df_2020[df_2020[cons_commune] == df_max]
df_max_ville_2020 = df_max_ville_2020['Nom de la commune'].unique().tolist()
df_max_ville_2020.append(df_max)

df_max = df_2021[cons_commune].max()
df_max_ville_2021 = df_2021[df_2021[cons_commune] == df_max]
df_max_ville_2021 = df_max_ville_2021['Nom de la commune'].unique().tolist()
df_max_ville_2021.append(df_max)

# Commune qui consomme le moins dans l'année:

df_min = df_2018[cons_commune].min()
df_min_ville_2018 = df_2018[df_2018[cons_commune] == df_min]
df_min_ville_2018 = df_min_ville_2018['Nom de la commune'].unique().tolist()
df_min_ville_2018.append(df_min)

df_min = df_2018[cons_commune].min()
df_min_ville_2019 = df_2019[df_2019[cons_commune] == df_min]
df_min_ville_2019 = df_min_ville_2019['Nom de la commune'].unique().tolist()
df_min_ville_2019.append(df_min)

df_min = df_2020[cons_commune].min()
df_min_ville_2020 = df_2020[df_2020[cons_commune] == df_min]
df_min_ville_2020 = df_min_ville_2020['Nom de la commune'].unique().tolist()
df_min_ville_2020.append(df_min)

df_min = df_2021[cons_commune].min()
df_min_ville_2021 = df_2021[df_2021[cons_commune] == df_min]
df_min_ville_2021 = df_min_ville_2021['Nom de la commune'].unique().tolist()
df_min_ville_2021.append(df_min)


def Elec_Adresse(Commune, Adresse, Annee, type):
    """"Donne la consommation annuelle de cette adresse en MHW
    Commune(string):nom de la commune
    Adresse(string):nom de l'adresse
    Annee(int):date de l'année
    type(string):Consommation annuelle total de l'adresse, Consommation annuelle moyenne par logement
    return float"""

    if Annee == 2018:
        df_adr = df_2018[df_2018["Adresse"] == Adresse]
        df_adr = df_adr[df_adr["Nom de la commune"] == Commune]
        return(df_adr[type].values[0])
    if Annee == 2019:
        df_adr = df_2019[df_2019["Adresse"] == Adresse]
        df_adr = df_adr[df_adr["Nom de la commune"] == Commune]
        return(df_adr[type].values[0])
    if Annee == 2020:
        df_adr = df_2020[df_2020["Adresse"] == Adresse]
        df_adr = df_adr[df_adr["Nom de la commune"] == Commune]
        return(df_adr[type].values[0])
    if Annee == 2021:
        df_adr = df_2021[df_2021["Adresse"] == Adresse]
        df_adr = df_adr[df_adr["Nom de la commune"] == Commune]
        return(df_adr[type].values[0])


def Elec_Commune(Commune, Annee):
    """"Donne la consommation annuelle moyenne de la commune en MHW
    Commune(string):nom de la commune
    Annee(int):date de l'année
    return float"""
    if Annee == 2018:
        df_com = df_2018[df_2018["Nom de la commune"] == Commune]
        return(round(df_com[cons_commune].mean(), 3))
    if Annee == 2019:
        df_com = df_2019[df_2019["Nom de la commune"] == Commune]
        return(round(df_com[cons_commune].mean(), 3))
    if Annee == 2020:
        df_com = df_2020[df_2020["Nom de la commune"] == Commune]
        return(round(df_com[cons_commune].mean(), 3))
    if Annee == 2021:
        df_com = df_2021[df_2021["Nom de la commune"] == Commune]
        return(round(df_com[cons_commune].mean(), 3))


def Elec_Departement(Departement, Annee):
    """"Donne la consommation annuelle moyenne du departement en MHW
    Departement(int):numero du departement
    Annee(int):date de l'année
    return float"""
    if Annee == 2018:
        df_dep = df_2018[df_2018['Departement'] == Departement]
        return(sum(df_dep[cons_commune].unique()))
    if Annee == 2019:
        df_dep = df_2019[df_2019['Departement'] == Departement]
        return(sum(df_dep[cons_commune].unique()))
    if Annee == 2020:
        df_dep = df_2020[df_2020['Departement'] == Departement]
        return(sum(df_dep[cons_commune].unique()))
    if Annee == 2021:
        df_dep = df_2021[df_2021['Departement'] == Departement]
        return(sum(df_dep[cons_commune].unique()))


Regions = {'Alsace': [67, 68],
           'Aquitaine': [24, 33, 40, 47, 64],
           'Auvergne': [3, 15, 43, 63],
           'Basse-Normandie': [14, 50, 61],
           'Bourgogne': [21, 58, 71, 89],
           'Bretagne': [22, 29, 35, 56],
           'Centre': [18, 28, 36, 37, 41, 45],
           'Champagne-Ardenne': [8, 10, 51, 52],
           'Franche-Comté': [25, 39, 70, 90],
           'Haute-Normandie': [27, 76],
           'Ile-de-France': [75, 77, 78, 91, 92, 93, 94, 95],
           'Languedoc-Roussillon': [11, 30, 34, 48, 66],
           'Limousin': [19, 23, 87],
           'Lorraine': [54, 55, 57, 88],
           'Midi-Pyrénées': [9, 12, 31, 32, 46, 65, 81, 82],
           'Nord-Pas-de-Calais': [59, 62],
           'Pays de la Loire': [44, 49, 53, 72, 85],
           'Picardie': [2, 60, 80],
           'Poitou-Charentes': [16, 17, 79, 86],
           "Provence-Alpes-Côte-d'Azur": [4, 5, 6, 13, 83, 84],
           'Rhône-Alpes': [1, 7, 26, 38, 42, 69, 73, 74]

           }


def Elec_Region(Region, Annee):
    """"Donne la consommation annuelle moyenne de la region en MHW
    Region(str):nom de la region (Avec leur majuscule)
    Annee(int):date de l'année
    return float"""
    ElecReg = 0
    for k in range(Regions.keys()):
        if k == Region:
            for i in range(Regions[Region]):
                ElecReg += Elec_Departement(i, Annee)
    return (ElecReg)


# Dictionnaire Departement,Conso par année

Elec_Par_Departement_2018 = {}
Elec_Par_Departement_2019 = {}
Elec_Par_Departement_2020 = {}
Elec_Par_Departement_2021 = {}
for i in range(1, 96):
    Elec_Par_Departement_2018[i] = Elec_Departement(i, 2018)
    Elec_Par_Departement_2019[i] = Elec_Departement(i, 2019)
    Elec_Par_Departement_2020[i] = Elec_Departement(i, 2020)
    Elec_Par_Departement_2021[i] = Elec_Departement(i, 2021)

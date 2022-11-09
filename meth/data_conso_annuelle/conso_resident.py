import pandas as pd
import numpy as np

#Test push


df = pd.read_csv(
    "consommation-annuelle-residentielle-par-adresse.csv", sep=';')
cons_total = "Consommation annuelle totale de l'adresse (MWh)"
cons_moyen = "Consommation annuelle moyenne par logement de l'adresse (MWh)"
cons_commune = "Consommation annuelle moyenne de la commune (MWh)"
df = df.drop("Code IRIS", axis=1)

# Donnée par année
df_2018 = df[df['Année'] == 2018]
df_2019 = df[df['Année'] == 2019]
df_2020 = df[df['Année'] == 2020]
df_2021 = df[df['Année'] == 2021]

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
    
Elec_Par_Departement_2018 = {}
Elec_Par_Departement_2019 = {}
Elec_Par_Departement_2020 = {}
Elec_Par_Departement_2021 = {}
for i in range (1,96):
    Elec_Par_Departement_2018[i] = Elec_Departement(i,2018)
    Elec_Par_Departement_2019[i] = Elec_Departement(i,2019)
    Elec_Par_Departement_2020[i] = Elec_Departement(i,2020)
    Elec_Par_Departement_2021[i] = Elec_Departement(i,2021)

    

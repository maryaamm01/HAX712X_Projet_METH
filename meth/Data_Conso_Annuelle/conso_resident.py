import pandas as pd
import numpy as np
df = pd.read_csv("consommation-annuelle-residentielle-par-adresse.csv",sep=';')
cons_total = "Consommation annuelle totale de l'adresse (MWh)"
cons_moyen = "Consommation annuelle moyenne par logement de l'adresse (MWh)"
cons_commune = "Consommation annuelle moyenne de la commune (MWh)"
df = df.drop("Code IRIS", axis=1)
df_2018=df[df['Année'] == 2018]
df_2019=df[df['Année'] == 2019]
df_2020=df[df['Année'] == 2020]
df_2021=df[df['Année'] == 2021]

def Elec_Adresse(Commune,Adresse,Annee,type):
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


import pandas as pd

cons_total = "Consommation annuelle totale de l'adresse (MWh)"
cons_moyen = "Consommation annuelle moyenne par logement de l'adresse (MWh)"
cons_commune = "Consommation annuelle moyenne de la commune (MWh)"

# Donnée par année
df_2018 = pd.read_csv("./data_conso_annuelle/consommation-annuelle-residentielle-par-adresse2018.csv", sep=';')
df_2019 = pd.read_csv("./data_conso_annuelle/consommation-annuelle-residentielle-par-adresse2019.csv", sep=';')
df_2020 = pd.read_csv("./data_conso_annuelle/consommation-annuelle-residentielle-par-adresse2020.csv", sep=';')
df_2021 = pd.read_csv("./data_conso_annuelle/consommation-annuelle-residentielle-par-adresse2021.csv", sep=';')

all_df = {"2018": df_2018, "2019": df_2019, "2020": df_2020, "2021": df_2021}

# Nettoyage des données (déja fait dans les .csv du github)
# df_2018 = df_2018.drop(['Code IRIS', 'Numéro de voie', 'Indice de répétition',
#                       'Type de voie', 'Libellé de voie', 'Segment de client',
#                        'Tri des adresses','Année','Nom IRIS'], axis=1)
#
# df_2019 = df_2019.drop(['Code IRIS', 'Numéro de voie', 'Indice de répétition',
#                       'Type de voie', 'Libellé de voie', 'Segment de client',
#                        'Tri des adresses','Année','Nom IRIS'], axis=1)
#
# df_2020 = df_2020.drop(['Code IRIS', 'Numéro de voie', 'Indice de répétition',
#                       'Type de voie', 'Libellé de voie', 'Segment de client',
#                        'Tri des adresses','Année','Nom IRIS'], axis=1)
#
# df_2021 = df_2021.drop(['Code IRIS', 'Numéro de voie', 'Indice de répétition',
#                       'Type de voie', 'Libellé de voie', 'Segment de client',
#                        'Tri des adresses','Année','Nom IRIS'], axis=1)


# Création département
df_2018['Departement'] = df_2018['Code INSEE de la commune']
df_2019['Departement'] = df_2019['Code INSEE de la commune']
df_2020['Departement'] = df_2020['Code INSEE de la commune']
df_2021['Departement'] = df_2021['Code INSEE de la commune']
# df['Departement'] = df['Departement'].apply(get_2_digit)
df_2018['Departement'] = df_2018['Departement'].apply(
    lambda x: (x // 10 ** 4 % 10) * 10 + (x // 10 ** 3 % 10))
df_2019['Departement'] = df_2019['Departement'].apply(
    lambda x: (x // 10 ** 4 % 10) * 10 + (x // 10 ** 3 % 10))
df_2020['Departement'] = df_2020['Departement'].apply(
    lambda x: (x // 10 ** 4 % 10) * 10 + (x // 10 ** 3 % 10))
df_2021['Departement'] = df_2021['Departement'].apply(
    lambda x: (x // 10 ** 4 % 10) * 10 + (x // 10 ** 3 % 10))


def calc_ranking(year: int, minimum: bool = True, size: int = 3):
    """
    Calculates a city ranking of the specified size
    @param year: The year
    @param minimum: True for min, False for max (default: True)
    @param size: The ranking size (default: 3)
    @return: A list containing ordered dicts with both city name and consumption value
    """
    ranking = []
    df_temp = all_df[str(year)].drop_duplicates('Code INSEE de la commune')
    df_temp = df_temp.sort_values(by=cons_commune, ascending=minimum).head(size)
    for i, row in df_temp.iterrows():
        ranking.append({"city": row['Nom de la commune'], "value": row[cons_commune]})
    return ranking


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
        return (df_adr[type].values[0])
    if Annee == 2019:
        df_adr = df_2019[df_2019["Adresse"] == Adresse]
        df_adr = df_adr[df_adr["Nom de la commune"] == Commune]
        return (df_adr[type].values[0])
    if Annee == 2020:
        df_adr = df_2020[df_2020["Adresse"] == Adresse]
        df_adr = df_adr[df_adr["Nom de la commune"] == Commune]
        return (df_adr[type].values[0])
    if Annee == 2021:
        df_adr = df_2021[df_2021["Adresse"] == Adresse]
        df_adr = df_adr[df_adr["Nom de la commune"] == Commune]
        return (df_adr[type].values[0])


def Elec_Commune(Commune, Annee):
    """"Donne la consommation annuelle moyenne de la commune en MHW
    Commune(string):nom de la commune
    Annee(int):date de l'année
    return float"""
    if Annee == 2018:
        df_com = df_2018[df_2018["Nom de la commune"] == Commune]
        return (round(df_com[cons_commune].mean(), 3))
    if Annee == 2019:
        df_com = df_2019[df_2019["Nom de la commune"] == Commune]
        return (round(df_com[cons_commune].mean(), 3))
    if Annee == 2020:
        df_com = df_2020[df_2020["Nom de la commune"] == Commune]
        return (round(df_com[cons_commune].mean(), 3))
    if Annee == 2021:
        df_com = df_2021[df_2021["Nom de la commune"] == Commune]
        return (round(df_com[cons_commune].mean(), 3))


def Elec_Departement(Departement, Annee):
    """"Donne la consommation annuelle moyenne du departement en MHW
    Departement(int):numero du departement
    Annee(int):date de l'année
    return float"""
    if Annee == 2018:
        df_dep = df_2018[df_2018['Departement'] == Departement]
        return (sum(df_dep[cons_commune].unique()))
    if Annee == 2019:
        df_dep = df_2019[df_2019['Departement'] == Departement]
        return (sum(df_dep[cons_commune].unique()))
    if Annee == 2020:
        df_dep = df_2020[df_2020['Departement'] == Departement]
        return (sum(df_dep[cons_commune].unique()))
    if Annee == 2021:
        df_dep = df_2021[df_2021['Departement'] == Departement]
        return (sum(df_dep[cons_commune].unique()))


regions = {
    "Auvergne-Rhône-Alpes": [1, 3, 7, 15, 26, 38, 42, 43, 63, 69, 73, 74],
    "Bourgogne-Franche-Comté": [21, 25, 39, 58, 70, 71, 89, 90],
    "Bretagne": [22, 29, 35, 56],
    "Centre-Val de Loire": [18, 28, 36, 37, 41, 45],
    "Grand Est": [8, 10, 51, 52, 54, 55, 57, 67, 68, 88],
    "Hauts-de-France": [2, 59, 60, 62, 80],
    "Île-de-France": [75, 77, 78, 91, 92, 93, 94, 95],
    "Normandie": [14, 27, 50, 61, 76],
    "Nouvelle-Aquitaine": [16, 17, 19, 23, 24, 33, 40, 47, 64, 79, 86, 87],
    "Occitanie": [9, 11, 12, 30, 31, 32, 34, 46, 48, 65, 66, 81, 82],
    "Pays de la Loire": [44, 49, 53, 72, 85],
    "Provence-Alpes-Côte d'Azur": [4, 5, 6, 13, 83, 84]
}


def Elec_Region(region: str, year: int) -> float:
    """"
    Calculates electricity consumption for the specified region
    @param region: The region from which we want to get the electricity consumption (str)
    @return: The electricity consumption (float)
    """
    return sum([Elec_Departement(dpt, year) for dpt in regions[region]])


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

ranking = {}
for year in range(2018, 2022):
    ranking[str(year)] = {"min": calc_ranking(year), "max": calc_ranking(year, False)}

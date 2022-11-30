from typing import Any

import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium

from data_conso_annuelle.conso_resident import Elec_Departement, Elec_Commune

granularities = {
    "communes": 'visualization/communes-version-simplifiee.geojson',
    "departements": 'visualization/departements-version-simplifiee.geojson',
    "regions": 'visualization/regions-version-simplifiee.geojson'
}

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
    "Provence-Alpes-Côte d'Azur": [4, 5, 6, 13, 83, 84],
}

APP_TITLE = "Carte"
APP_SUB_TITLE = "Consommation d'électricité en France"

YEARS = [2018, 2019, 2020, 2021]

st.set_page_config(APP_TITLE)
st.title(APP_TITLE)
st.caption(APP_SUB_TITLE)

YEAR = 2020


def get_region_consumption(region: str) -> float:
    return sum([Elec_Departement(dpt, YEAR) for dpt in regions[region]])


def display(granularity: str, dataframe: Any, key: str = 'nom'):
    territory_map = folium.Map(location=[46.8534, 2.3488], zoom_start=5, scrollWheelZoom=False,
                               tiles='CartoDB positron')

    choropleth = folium.Choropleth(
        geo_data=gpd.read_file(granularities[granularity], encoding="utf-8"),
        key_on=f'feature.properties.{key}',
        data=dataframe,
        columns=("nom", "cons"),
        line_opacity=0.8,
        highlight=True
    )
    choropleth.geojson.add_to(territory_map)

    df_indexed = dataframe.set_index("nom")
    for feature in choropleth.geojson.data['features']:
        df_col = feature["properties"][key]
        feature['properties']['cons'] = f"Consommation : " \
                                        f"{df_indexed.loc[df_col][0] if df_col in list(df_indexed.index) else 0:.3f} " \
                                        f"MWh"

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(["nom", "cons"], labels=False)
    )

    st_folium(territory_map, width=700, height=450)


dataset = {"nom": regions.keys(), "cons": [get_region_consumption(region) for region in regions.keys()]}
df = pd.DataFrame.from_dict(dataset)
display("regions", df)

dataset = {"nom": [str(i) if i > 9 else f"0{i}" for i in range(96)],
           "cons": [Elec_Departement(i, YEAR) for i in range(96)]}
df = pd.DataFrame.from_dict(dataset)
display("departements", df, "code")
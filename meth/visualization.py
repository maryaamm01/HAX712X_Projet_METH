from typing import Any # Accented characters

import pandas as pd # Data
import geopandas as gpd # Geographic Data
import folium # Map
import streamlit as st # Visualizing the maps on a browser page
from streamlit_folium import st_folium # Visualizing the maps on a browser page

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
    "Provence-Alpes-Côte d'Azur": [4, 5, 6, 13, 83, 84]
}

YEAR = 2018
grain = "communes"

# Streamlit app parameters
APP_TITLE = "Carte de la consommation d'électricité en France (MWh)"

st.set_page_config(APP_TITLE)
st.title(APP_TITLE)


def get_region_consumption(region: str) -> float:
    """"
    Calculates electricity consumption for the specified region
    @param region: The region from which we want to get the electricity consumption (str)
    @return: The electricity consumption (float)
    """
    return sum([Elec_Departement(dpt, YEAR) for dpt in regions[region]])


def display(granularity: str, dataframe: Any, key: str = 'nom'):
    """Displays a choropleth map showing the French electricity consumption,
    the regions of the map being displayed according to the specified granularity.
    @param: granularity: "communes", "departements" or "regions".
    @param: dataframe: the dataset used to color the choropleth map, converted to a dataframe.
    """
    # Creating the map and getting folium to focus on the right place (France)
    territory_map = folium.Map(location=[46.8534, 2.3488], zoom_start=5, scrollWheelZoom=False,
                               tiles='CartoDB positron')

    # Adding data to the map
    choropleth = folium.Choropleth(
        geo_data=gpd.read_file(granularities[granularity], encoding="utf-8"),
        key_on=f'feature.properties.{key}',
        data=dataframe,
        columns=("nom", "cons"),
        line_opacity=0.8,
        highlight=True
    )
    choropleth.geojson.add_to(territory_map)

    # Adding labels to the regions
    df_indexed = dataframe.set_index("nom")
    for feature in choropleth.geojson.data['features']:
        df_col = feature["properties"][key]
        feature['properties']['cons'] = f"Consommation : " \
                                        f"{df_indexed.loc[df_col][0] if df_col in list(df_indexed.index) else 0:.3f} " \
                                        f"MWh"

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(["nom", "cons"], labels=False)
    )

    st_folium(territory_map, width=700, height=450) # Plotting in the streamlit app

def disp(granularity: str):
    if granularity == "regions":
        APP_SUB_TITLE = "Année : " + str(YEAR) + ", " + "Granularité : " + grain
        st.caption(APP_SUB_TITLE)
        dataset = {"nom": regions.keys(), "cons": [get_region_consumption(region) for region in regions.keys()]}
        df = pd.DataFrame.from_dict(dataset)
        display(granularity, df)

    elif granularity == "departements": ##A COMPLETER : Zoom sur la région, spécifier la région en subtitle
        APP_SUB_TITLE = "Année : " + str(YEAR) + ", " + "Granularité : " + grain + ", Region : "
        st.caption(APP_SUB_TITLE)
        dataset = {"nom": [str(i) if i > 9 else f"0{i}" for i in range(96)],
                       "cons": [Elec_Departement(i, YEAR) for i in range(96)]}
        df = pd.DataFrame.from_dict(dataset)
        display("departements", df, "code")


# "Main"
disp(grain)

from typing import Any  # Accented characters

import folium  # Map
import geopandas as gpd  # Geographic Data
import pandas as pd  # Data
import streamlit as st  # Visualizing the maps on a browser page
from streamlit_folium import st_folium  # Visualizing the maps on a browser page

from data_conso_annuelle.conso_resident import Elec_Departement, Elec_Region as get_region_consumption
from data_conso_annuelle.conso_resident import regions, ranking

granularities = {
    "Municipalities": 'visualization/communes-version-simplifiee.geojson',
    "Departments": 'visualization/departements-version-simplifiee.geojson',
    "Regions": 'visualization/regions-version-simplifiee.geojson'
}


def display(granularity: str, dataframe: Any, key: str = 'nom'):
    """Displays a choropleth map showing the French electricity consumption,
    the regions of the map being displayed according to the specified granularity.
    @param: granularity: "Municipalities", "Departments" or "Regions".
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

    st_folium(territory_map, width=700, height=450)  # Plotting in the streamlit app


def load(granularity: str, year: int):
    """

    @param granularity:
    @param year:
    @return:
    """
    if granularity == "Regions":
        dataset = {"nom": regions.keys(), "cons": [get_region_consumption(region, year) for region in regions.keys()]}
        df = pd.DataFrame.from_dict(dataset)
        display(granularity, df)
    elif granularity == "Departments":
        dataset = {"nom": [str(i) if i > 9 else f"0{i}" for i in range(96)],
                   "cons": [Elec_Departement(i, year) for i in range(96)]}
        df = pd.DataFrame.from_dict(dataset)
        display(granularity, df, "code")


def disp_top_3(year: int, order: str = "min"):
    """
    Displays a top 3 of the least/most electricity consuming towns.
    @param year: which year for the top 3
    @param order: "min" for least consuming, "max" for most consuming (default: "min")
    """
    if order == "min":
        st.subheader("Top 3 Most Eco-Friendly Towns:")
    elif order == "max":
        st.subheader("Top 3 Most Electricity Consuming Towns:")
    for i, city in enumerate(ranking[str(year)][order]):
        st.metric(f'#{i + 1}: {city["city"]}', f'{city["value"]} MWh')


def main():
    # Streamlit app parameters
    APP_TITLE = "French electricity consumption map"
    st.set_page_config(APP_TITLE, layout="wide")
    st.title(APP_TITLE)

    year = [2018, 2019, 2020, 2021]
    selected_year = st.sidebar.selectbox('Year', year)
    selected_granularity = st.sidebar.radio('Granularity', ["Regions", "Departments", "Municipalities"])

    # Displays
    col1, col2 = st.columns(spec=[3, 1], gap="small")
    with col1:
        APP_SUB_TITLE = f'Year : {selected_year}, Granularity: {selected_granularity}, Unit: MWh'
        st.caption(APP_SUB_TITLE)
        load(selected_granularity, selected_year)
    with col2:
        disp_top_3(selected_year, "min")
        disp_top_3(selected_year, "max")


if __name__ == "__main__":
    main()

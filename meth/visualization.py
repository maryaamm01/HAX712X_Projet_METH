from typing import Any  # Accented characters

import folium  # Map
import geopandas as gpd  # Geographic Data
import pandas as pd  # Data
import streamlit as st  # Visualizing the maps on a browser page
from streamlit_folium import st_folium  # Visualizing the maps on a browser page

from data_conso_annuelle.conso_resident import Elec_Departement, Elec_Region as get_region_consumption
from data_conso_annuelle.conso_resident import granularities, regions, ranking


def display(granularity: str, dataframe: Any, key: str = 'nom', zoom: float = 5, lat: float = 46.8534,
            long: float = 2.3488):
    """
    To be used in load_... functions.
    Displays a choropleth map showing the French electricity consumption,
    the regions of the map being displayed according to the specified granularity.
    @param: granularity: "Departments", "Regions" or (coming soon) "Municipalities".
    @param: dataframe: the dataset used to color the choropleth map, converted to a dataframe.
    @return: A dict with 'region': the name of the clicked area and 'coordinates': the latitude and longitude of the click (dict 'lat', 'lng').
    """
    # Creating the map and getting folium to focus on the right place (France)
    territory_map = folium.Map(location=[lat, long], zoom_start=zoom, scrollWheelZoom=False,
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

    final_map = st_folium(territory_map, width=700, height=450)  # Plotting in the streamlit app

    # Returning parameters that we are going to use later to make the maps interactive
    reg_name = ''
    if final_map['last_active_drawing']:  # To get the clicked area
        reg_name = final_map['last_active_drawing']['properties']['nom']

    if final_map['last_clicked']:  # To get the click position
        click = {"lat": final_map['last_clicked']['lat'], "lng": final_map['last_clicked']['lng']}
    else:
        click = {"lat": 46, "lng": 2.3}
    return {"region": reg_name, "coordinates": click}


def load_regions(year: int):
    """
    To be used to display regions.
    @param year: The year of the data
    @return: The parameters returned by the display function
    """
    dataset = {"nom": regions.keys(), "cons": [get_region_consumption(region, year) for region in regions.keys()]}
    df = pd.DataFrame.from_dict(dataset)
    return display("Regions", df)


def load_department(year: int, reg: str = "Nouvelle-Aquitaine", zoom: float = 5, lat: float = 46.8534,
                    long: float = 2.3488):
    """
    To be used to display departments.
    @param year: The year of the data
    @param reg: The region whose departments you want to load
    @param zoom: The zoom (5 for national scale, 6.5 for region scale)
    @param lat: The latitude of the map center
    @param long: The longitude of the map center
    @return: The parameters returned by the display function
    """
    if reg == '':
        reg = "Nouvelle-Aquitaine"
        lat = 46.8534
        long = 2.3488
    dataset = {"nom": [str(i) if i > 9 else f"0{i}" for i in regions[f'{reg}']],
               "cons": [Elec_Departement(i, year) for i in regions[f'{reg}']]}
    df = pd.DataFrame.from_dict(dataset)
    (lat, long) = (46.8534, 2.3488) if zoom == 5 else (lat, long)
    display("Departments", df, "code", zoom, lat, long)


def display_reg_filter(reg_name: str):
    """
    Creates a scroll bar to select a region
    @param reg_name: the active parameter
    @return: the scroll bar
    """
    reg_list = [''] + list(regions)
    reg_index = reg_list.index(reg_name) if reg_name and reg_name in reg_list else 0
    return st.sidebar.selectbox('Region', reg_list, reg_index)


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


def set_zoom(cond):
    """
    Really just gets the zoom for load_department for now.
    @param cond: The condition for zooming
    @return: the zoom level
    """
    return 5 if cond else 6.5


def main(lat_value1: int, lat_value2: int):
    # Streamlit app parameters
    APP_TITLE = "French electricity consumption map"
    st.set_page_config(APP_TITLE, layout="wide")
    st.title(APP_TITLE)

    # Displays
    year = [2018, 2019, 2020, 2021]
    selected_year = st.sidebar.selectbox('Year', year)
    col1, col2 = st.columns(spec=[3, 1], gap="small")
    with col1:
        APP_SUB_TITLE = f'Year : {selected_year}, Unit: MWh'
        st.caption(APP_SUB_TITLE)

        loaded_reg = load_regions(selected_year)
        selected_region = display_reg_filter(loaded_reg['region'])

        flag = round(float(lat_value1), 2) == round(loaded_reg['coordinates']['lat'], 2) \
               and round(float(lat_value2), 2) == round(loaded_reg['coordinates']['lat'], 2)
        default_zoom = set_zoom(flag)

        load_department(selected_year,
                        selected_region,
                        default_zoom,
                        loaded_reg['coordinates']['lat'],
                        loaded_reg['coordinates']['lng'])
    with col2:
        disp_top_3(selected_year, "min")
        disp_top_3(selected_year, "max")

    return loaded_reg['coordinates']['lat']


if __name__ == "__main__":
    file_path = "visualization/log.txt"

    with open(file_path, "r+") as f:
        first_line = f.readline()
        while first_line == "\n":
            first_line = f.readline()
        second_line = f.readline()

    if second_line == '':
        second_line = 46.8534

    lat_value = main(first_line, second_line)

    with open(file_path, "w") as f:
        f.write(f'{second_line}\n{lat_value}')

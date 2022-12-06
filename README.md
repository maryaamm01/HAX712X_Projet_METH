# HAX712X_Projet_METH

This project handles datasets from the French electricity consumption with the motivation:
- to create a graphic interface for vizualizing French electricity consumption on a past given day, month or year;
- to predict electricity consumption on a future day.

## Sources

The datasets we used are available at:
- [opendatasoft](https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/information/?disjunctive.nature&sort=-date_heure) (dataset for prediction)
- https://www.rte-france.com/eco2mix/telecharger-les-indicateurs (dataset for prediction)
- [enedis](https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/information/) (dataset for visualization)
- [france-geojson](https://github.com/gregoiredavid/france-geojson/blob/master/README.md) (dataset for plotting France)

## Installation and configuration

To install the requirements, please use the following command: 

    pip install -r requirements.txt

## Use

To run the visualization, make sure you are in the /meth folder, then use:

    streamlit run visualization.py

## References

- Zakaria Chowdhury, [streamlit-map-dashboard](https://github.com/zakariachowdhury/streamlit-map-dashboard)

## Licence

We do not have a licence yet.

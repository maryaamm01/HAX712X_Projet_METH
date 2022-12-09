# HAX712X_Projet_METH

This project handles datasets from the French electricity consumption with the motivation:
- to create a graphic interface for vizualizing French electricity consumption on a past given day, month or year;
- to predict electricity consumption on a future day.

## Installation and configuration

To install the requirements, please use the following command: 

    pip install -r requirements.txt

## Use

To run the visualization, make sure you are in the /meth folder, then use:

    streamlit run visualization.py
    
You can find the december 8th electricity consumption prediction data (total consumption) in the cons_08_dec.csv file

You can find the december 8th prediction data for each energy type in the energies_prediction_8_dec.ipynb file. 

## References

- Zakaria Chowdhury, [streamlit-map-dashboard](https://github.com/zakariachowdhury/streamlit-map-dashboard)
- VarishuPant99, [UCM Model](https://github.com/VarishuPant99/Unobserved_Components_Model/blob/master/ECM_Varishu_Pant_D19033.ipynb)


## Sources

The datasets we used are available at:
- [opendatasoft](https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/information/?disjunctive.nature&sort=-date_heure) (dataset for prediction)
- [eco2mix](https://www.rte-france.com/eco2mix/telecharger-les-indicateurs) (dataset for prediction)
- [enedis](https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/information/) (dataset for visualization)
- [france-geojson](https://github.com/gregoiredavid/france-geojson/blob/master/README.md) (dataset for plotting France)


## Known Issues

**[FIXED] "Can't convert "\n" to float" when running the visualization.**

How to fix : 
If you still get this error, please check the file log.txt in your meth/visualization folder. It is due to the blank spaces at the begining of the file, please remove these and make sure you only have two values, on two separate lines, like this:
    
    46.8534
    46.8534


## Licence

We do not have a licence yet.

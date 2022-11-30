from visualization.ChoroMap import ChoroMap
from data_conso_annuelle.conso_resident import Data
import urllib.request
import json


#Les 100 premières lignes de chaque base de données
data2018 = urllib.request.urlopen("https://data.enedis.fr/api/records/1.0/search/?dataset=consommation-annuelle-residentielle-par-adresse&q=&rows=100&facet=annee&facet=nom_iris&facet=numero_de_voie&facet=indice_de_repetition&facet=type_de_voie&facet=libelle_de_voie&facet=code_commune&facet=nom_commune&facet=nombre_de_logements&facet=adresse&facet=tri_des_adresses&refine.annee=2018").read()
data2019 = urllib.request.urlopen("https://data.enedis.fr/api/records/1.0/search/?dataset=consommation-annuelle-residentielle-par-adresse&q=&rows=100&facet=annee&facet=nom_iris&facet=numero_de_voie&facet=indice_de_repetition&facet=type_de_voie&facet=libelle_de_voie&facet=code_commune&facet=nom_commune&facet=nombre_de_logements&facet=adresse&facet=tri_des_adresses&refine.annee=2019").read()
data2020 = urllib.request.urlopen("https://data.enedis.fr/api/records/1.0/search/?dataset=consommation-annuelle-residentielle-par-adresse&q=&rows=100&facet=annee&facet=nom_iris&facet=numero_de_voie&facet=indice_de_repetition&facet=type_de_voie&facet=libelle_de_voie&facet=code_commune&facet=nom_commune&facet=nombre_de_logements&facet=adresse&facet=tri_des_adresses&refine.annee=2020").read()
data2021 = urllib.request.urlopen("https://data.enedis.fr/api/records/1.0/search/?dataset=consommation-annuelle-residentielle-par-adresse&q=&rows=100&facet=annee&facet=nom_iris&facet=numero_de_voie&facet=indice_de_repetition&facet=type_de_voie&facet=libelle_de_voie&facet=code_commune&facet=nom_commune&facet=nombre_de_logements&facet=adresse&facet=tri_des_adresses&refine.annee=2021").read()

#Nos objets "Data" (on pourrait le renommer)
conso2018 = Data(data2018)
conso2019 = Data(data2019)
conso2020 = Data(data2020)
conso2021 = Data(data2021)

cons_commune_mhw = "consommation_annuelle_totale_de_l_adresse_mwh"

#Test
#print(conso2020.getMax(cons_commune_mhw))
#print(conso2020.getMin(cons_commune_mhw))

cm = ChoroMap()
# cm = ChoroMap(2) #Constructeur par échelle
# cmTest = ChoroMap(2)
# cm = ChoroMap(cmTest) #Constructeur par copie
# cm = ChoroMap("data/france_geojson/metropole.geojson") #Constructeur par geojson

# Erreurs :
# cm = ChoroMap(3) #Erreur constructeur par échelle
# cm = ChoroMap("hello") #Erreur constructeur par geojson

#cm.cm_show()

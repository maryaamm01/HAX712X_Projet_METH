from visualization.ChoroMap import ChoroMap

# Constructeurs :
cm = ChoroMap()  # Constructeur par défaut
test = "test"
# cm = ChoroMap(2) #Constructeur par échelle
# cmTest = ChoroMap(2)
# cm = ChoroMap(cmTest) #Constructeur par copie
# cm = ChoroMap("data/france_geojson/metropole.geojson") #Constructeur par geojson

# Erreurs :
# cm = ChoroMap(3) #Erreur constructeur par échelle
# cm = ChoroMap("hello") #Erreur constructeur par geojson

cm.cm_show()

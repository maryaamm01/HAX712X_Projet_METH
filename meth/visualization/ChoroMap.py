import geopandas as gpd
import matplotlib.pyplot as plt

maps = ['meth/map_dataset/communes-version-simplifiee.geojson',
        'meth/map_dataset/departements-version-simplifiee.geojson',
        'meth/map_dataset/regions-version-simplifiee.geojson']


class ChoroMap():
    def __init__(self, *args):
        """Constructor of ChoroMap objects.

        Depending on args type:
        None -- the scale of the ChoroMap will be departmental.
        int -- the scale of the ChoroMap will adjust accordingly (0=town, 1=department, 2=region).
        ChoroMap -- builds a copy of an existing ChoroMap.
        str -- path for a geojson file. Builds a choroMap based on the specified geojson file. Not recommended
        """
        if len(args) > 0:
            # Builds the ChoroMap based on the specified scale (int)
            if isinstance(args[0], int):
                if args[0] < 0 or args[0] > 2:
                    raise Exception("ChoroMap __init__(arg): arg should be an integer between 0 and 2")
                self.map = gpd.read_file(maps[args[0]])

            # Builds the ChoroMap based on another ChoroMap (creates a copy)
            elif isinstance(args[0], ChoroMap):
                self.map = args[0].cm_get_map()

            # Builds the ChoroMap based on a specified geojson file (not recommended)
            if isinstance(args[0], str):
                if not (self.__is_a_geojson__(args[0])):
                    raise Exception("ChoroMap __init__(arg): arg should be the path to a geojson file (str)")
                self.map = gpd.read_file(args[0])

        # Builds the default ChoroMap
        else:
            self.map = gpd.read_file(maps[1])

    def cm_get_map(self):
        """Returns map attribute (GeoDataFrame from geopandas) of the ChoroMap object"""
        return self.map

    def cm_set_map(self, scale):
        """Sets the ChoroMap map attribute scale (0 for town, 1 for department, 2 for region"""
        if scale > 2 or scale < 1:
            raise Exception("ChoroMap cm_set_map(scale): scale should be an integer in range(0,2)")
        self.map = gpd.read_file(maps[scale])

    def cm_show(self):
        """Displays the ChoroMap in a separate window"""
        self.cm_get_map().plot()
        plt.show()

    def __is_a_geojson__(self, path):
        """Tests if path argument is the path to a geojson file"""
        if len(path) < 8:
            return False
        extension = ""
        for i in range(-8, 0):
            extension = extension + path[i]
        if extension != ".geojson":
            return False
        return True

# Constructeurs :
cm = ChoroMap()  # Constructeur par défaut
# cm = ChoroMap(2) #Constructeur par échelle
# cmTest = ChoroMap(2)
# cm = ChoroMap(cmTest) #Constructeur par copie
# cm = ChoroMap("data/france_geojson/metropole.geojson") #Constructeur par geojson

# Erreurs :
# cm = ChoroMap(3) #Erreur constructeur par échelle
# cm = ChoroMap("hello") #Erreur constructeur par geojson

cm.cm_show()
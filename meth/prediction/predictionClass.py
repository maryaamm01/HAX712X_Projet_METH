#%%
import pandas as pd
import warnings
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

class MODEL():
    """cette classe définit le modèle de prédiction nommé Unobserved Components Model "UCM" et cette
    se compose de deux fonctions la première c'est la fonction d'initialisation de l'objet  (__init__)
    avec les attributs de cette fonction sont :\\
      - start : c'est la date du début de prédiction de type date écrit sous la forme ANNÉE-MOIS exemple (2022-06)
      - end : c'est la date du fin de prédiction de type date écrit sous la forme ANNÉE-MOIS exemple (2022-09).
    la deuxième fonction nommé (mod) définit le modèle de prédiction UCM du premier temp cette fonction fait l'importation
    du data collectés du 01 JAN 2019 jusqu'à 06 Déc 2022 et cette fonction retourne forc:\\
      -for : c'est les valeure de prédiction cherché sous form data frame"""
    def __init__(self,start,end) -> None:
        self.start = start
        self.end = end
        pass
    def mod(self) :
        df =pd.read_csv("./dataset/dataelec.csv")  # data from 2019-01-01 00:00:00 to 2022-11-29 12:45:00
        df=df.set_index('Temps')
        df.index=pd.to_datetime(df.index)
        # splitting time series to train and test subsets
        data_test = df.iloc[-35880:, :]
        # Unobserved Components model definition
        model_UC1 = sm.tsa.UnobservedComponents(df,
                                                level='dtrend',
                                                irregular=True,
                                                stochastic_level=False,
                                                stochastic_trend=False,
                                                stochastic_freq_seasonal=[True, False, False],
                                                freq_seasonal=[{'period': 96, 'harmonics': 6},
                                                               {'period': 672,'harmonics': 2},
                                                               {'period': 35066, 'harmonics': 1}])
        # fitting model to train data
        model_UC1res = model_UC1.fit()
    
        forc = model_UC1res.predict(start=self.start+" 00:00:00", end=self.end+" 23:45:00").to_frame()
        return forc



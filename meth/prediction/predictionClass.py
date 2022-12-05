#%%
import CreationData as cr
import warnings
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
import pandas as pd
import numpy as np
# plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

class MODEL():

    def __init__(self,start,end) -> None:
        self.start = start
        self.end = end
        pass

    def mod(self) :
        df = cr.dataframe()  # data from 2019-01-01 00:00:00 to 2022-11-29 12:45:00
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
#%%
start1="2022-12-08"
end1="2022-12-08"
obj1 = MODEL(start=start1,end=end1)
day1 = obj1.mod()
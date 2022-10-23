# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:52:30 2022

@author: Slama
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from pandas.plotting import autocorrelation_plot
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

# importation DataFrame

chemin ="C:\\Users\\Slama\\Downloads\\eco2mix-national-tr.csv"
df= pd.read_csv(chemin, sep= ';')
# supprimer les colnnes initules 

Ndf = df.drop(df.loc[:,'Prévision J-1 (MW)':'Eolien offshore (MW)'].columns, axis = 1)
Ndf = Ndf.drop(['Nature','Date - Heure','Périmètre'], axis =1)

# changer le format du Date
time_improved = pd.to_datetime(Ndf['Date'] + ' ' + Ndf['Heure'] + ':00',
                               format='%Y-%m-%d %H:%M')
Ndf['Date_Heure']=time_improved

# supprimer colonnes 'Date','Heure' et on garde que 'Dtae_Heure' 
del Ndf['Date'],Ndf['Heure']

# supprimer les cases vides 
Ndf.dropna(inplace=True)

# ranger dataframe par rapport à la colonne "Date_Heure" et en même temps le choisit comme Index
Ndf=Ndf.set_index(['Date_Heure'])
Ndf=Ndf.sort_index(ascending=True)

# afficher la serie temporelle de la consommation
  # plt.plot(Ndf["Consommation (MW)"][:30],label='Consommation')
  
# fonction pour tester la stattionarité de notre dataFrame
def test_stationarity(timeseries):
    import matplotlib.pyplot as plt
    rolmean = timeseries.rolling(window=15).mean() 
    rolstd = timeseries.rolling(window=15).std()
    
    orig =plt.plot(timeseries,label='Data Original') # affichage de DataFrame
    mean =plt.plot(rolmean,label='la moyenne')# affichage de la moyenne
    std =plt.plot(rolstd,label='l’écart type')# affichage de l'écart type
    
    plt.legend(loc='best')
    plt.title("Ndf avec la moyenne et l'écart type")
    plt.show()
    
    from statsmodels.tsa.stattools import adfuller
    
    dftest = adfuller(timeseries)
    dfoutput = pd.Series(dftest[0:4], index =['the test statistic','Mackinnon approximate p-value','#usedlags','Nobs'])
    
    print(dfoutput)
print(test_stationarity(Ndf)) 

Ndf.dropna(inplace=True)
# la correlation actifs et passif
from statsmodels.tsa.stattools import acf,pacf 
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import matplotlib.pyplot as plt 

lag_acf=acf(Ndf,nlags=32)
lag_pacf=pacf(Ndf,nlags=16)

fig, ax=plt.subplots(1,2,figsize=(20,5))

plot_acf(lag_acf,ax=ax[0])
plot_pacf(lag_pacf,lags=7,ax=ax[1])
plt.show()
# Creation du Modéle de prédiction 
def predict(Ndf,p,d,q):
    from statsmodels.tsa.arima.model import ARIMA
    from sklearn.model_selection import train_test_split
    Ndf.dropna(inplace=True)
    train , test = train_test_split(Ndf, test_size=0.20,shuffle=False)
    
    model_arima = ARIMA(train,order=(p,d,q))
    model_arima_fit = model_arima.fit()
    predictions=model_arima_fit.predict(start='2022-10-10 00:00:00',end='2022-10-11 00:00:00') #exemple
    
    error = mean_squared_error(test, predictions)
    print('Test MSE %5' %error)
    predict = np.exp(predictions)
    test_set = np.exp(test)
    plt.plot(test_set)
    plt.plot(predict,color='red')
    plt.show()
    from pandas import DataFrame
    residual = DataFrame(model_arima_fit.resid)
    residual.plot(kind='kde')
    
    
# predict(Ndf, 0, d, q)(d et q à chercher)

"""   p détermine le nombre de termes autorégressifs (AR)
      d détermine l’ordre de différenciation
      q détermine le nombre de termes de moyenne mobile (MA) """

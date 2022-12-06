#%%
import numpy as np
import pandas as pd
import datetime
import numpy as np
import os
import pooch

def dataframe(energie):
    """Traitement de la base de donnees pour l'energie ciblé
    energie(str):Nom de l'energie du dataframe
    return dataframe"""
    
    #___________________Création du Data 2019_________________________
    url = "https://bit.ly/3i1OFkU"
    path_target = "./eco2mix-national-cons-def.csv"
    path, fname = os.path.split(path_target)
    pooch.retrieve(url, path=path, fname=fname, known_hash=None,)
    data2019= pd.read_csv("eco2mix-national-cons-def.csv",sep=";")
    data2019=data2019[['Date','Heure',energie]]
    ##changer le format du temps. 
    time_improved = pd.to_datetime(data2019['Date'] +
                                    ' ' + data2019['Heure'],
                                    format='%Y-%m-%d %H:%M')
    data2019['Temps'] = time_improved  
    data2019.set_index('Temps', inplace=True) 
    del data2019['Heure']
    del data2019['Date']
    data2019 = data2019.sort_index(ascending=True)
    ## remplacer les NaN et la transformation de la consomation du 2019 sur chaque 15 min.
    for nan in range(len(data2019)-1):  
        if data2019[[energie]].isna().iloc[:,0][nan]:
            data2019[energie][nan] = (data2019[energie][nan-1] +data2019[energie][nan+1])/2
    data2019[energie][len(data2019)-1]= (data2019[energie][len(data2019)-2]+data2019[energie][len(data2019)-3])/2        
    print("le nombre de NaN sur data2019 est : ",int(data2019.isna().sum())) 
    
    
    #____________________Création du Data 2020_________________________
    url = "https://bit.ly/3V81yIg"
    path_target = "./eco2mix-national-cons-def(1).csv"
    path, fname = os.path.split(path_target)
    pooch.retrieve(url, path=path, fname=fname, known_hash=None,)
    data2020 = pd.read_csv("eco2mix-national-cons-def(1).csv",sep=";")
    data2020 = data2020[['Date','Heure',energie]]
    ## changer le format du temps.
    time_improved = pd.to_datetime(data2020['Date'] +
                                    ' ' + data2020['Heure'],
                                    format='%Y-%m-%d %H:%M')
    data2020['Temps'] = time_improved  
    data2020.set_index('Temps', inplace=True) 
    del data2020['Heure']
    del data2020['Date']
    data2020 = data2020.sort_index(ascending=True)
    ## remplacer les NaN et la transformation de la consomation du 2020 sur chaque 15 min.
    for nan in range(len(data2020)-1):  
        if data2020[[energie]].isna().iloc[:,0][nan]:
            data2020[energie][nan] = (data2020[energie][nan-1] +data2020[energie][nan+1])/2
    data2020[energie][len(data2020)-1] = (data2020[energie][len(data2020)-2]+data2020[energie][len(data2020)-3])/2        
    print("le nombre de NaN sur data2020 est : ",int(data2020.isna().sum()))
    
    
    #____________________Création du Data 2021_________________________
    url = "https://bit.ly/3UO3NRc"
    path_target = "./eco2mix-national-cons-def(2).csv"
    path, fname = os.path.split(path_target)
    pooch.retrieve(url, path=path, fname=fname, known_hash=None,)
    data2021 = pd.read_csv("eco2mix-national-cons-def(2).csv",sep=";")
    data2021 = data2021[['Date','Heure',energie]]
    ## changer le format du temps .
    time_improved = pd.to_datetime(data2021['Date'] +
                                    ' ' + data2021['Heure'],
                                    format='%Y-%m-%d %H:%M')
    data2021['Temps'] = time_improved  
    data2021.set_index('Temps', inplace=True) 
    del data2021['Heure']
    del data2021['Date']
    data2021 = data2021.sort_index(ascending=True)
    ## remplacer les NaN et la transformation de la consomation du 2021 sur chaque 15 min.
    for nan in range(len(data2021)-1):  
        if data2021[[energie]].isna().iloc[:,0][nan]:
            data2021[energie][nan] = (data2021[energie][nan-1] +data2021[energie][nan+1])/2
    data2021[energie][len(data2021)-1]= (data2021[energie][len(data2021)-2]+data2021[energie][len(data2021)-3])/2        
    print("le nombre de NaN sur data2021 est : ",int(data2021.isna().sum()))
    #____________________Création du Data 2022 du janvier à mai_________________________
    url = "https://bit.ly/3gowmWv"
    path_target = "./eco2mix-national-cons-def(3).csv"
    path, fname = os.path.split(path_target)
    pooch.retrieve(url, path=path, fname=fname, known_hash=None,)
    data2022HALF1 = pd.read_csv("eco2mix-national-cons-def(3).csv",sep=";")
    #data2022HALF1 = data2022HALF1.set_index('Date et Heure')
    data2022HALF1 = data2022HALF1[['Date','Heure',energie]]
    ### changer le format du temps
    time_improved = pd.to_datetime(data2022HALF1['Date'] +
                                    ' ' + data2022HALF1['Heure'],
                                    format='%Y-%m-%d %H:%M')
    data2022HALF1['Temps'] = time_improved  
    data2022HALF1.set_index('Temps', inplace=True) 
    del data2022HALF1['Heure']
    del data2022HALF1['Date']
    data2022HALF1 = data2022HALF1.sort_index(ascending=True)
    ## remplacer les NaN et la transformation de la consomation du 2022 sur chaque 15 min.
    for nan in range(len(data2022HALF1)-1):  
        if data2022HALF1[[energie]].isna().iloc[:,0][nan]:
            data2022HALF1[energie][nan] = (data2022HALF1[energie][nan-1] +data2022HALF1[energie][nan+1])/2
    data2022HALF1[energie][len(data2022HALF1)-1] = (data2022HALF1[energie][len(data2022HALF1)-2]+data2022HALF1[energie][len(data2022HALF1)-3])/2        
    print("le nombre de NaN sur data2022HALF1 est : ",int(data2022HALF1.isna().sum())) 
    
    
    #____________________Création du Data 2022 de junin_________________________
    url = "https://bit.ly/3Ep9TjU"
    path_target = "./eco2mix-national-cons-def(4).csv"
    path, fname = os.path.split(path_target)
    pooch.retrieve(url, path=path, fname=fname, known_hash=None,)
    data2022HALF2 = pd.read_csv("eco2mix-national-cons-def(4).csv",sep=";")
    #Data2022 = Data2022.set_index('Date et Heure')
    data2022HALF2=data2022HALF2[['Date','Heure',energie]]
    ### changer le format du temps
    time_improved = pd.to_datetime(data2022HALF2['Date'] +
                                    ' ' + data2022HALF2['Heure'],
                                    format='%Y-%m-%d %H:%M')
    data2022HALF2['Temps'] = time_improved  
    data2022HALF2.set_index('Temps', inplace=True) 
    del data2022HALF2['Heure']
    del data2022HALF2['Date']
    data2022HALF2= data2022HALF2.sort_index(ascending=True)
    data2022HALF2=data2022HALF2.dropna()
    print("le nombre de NaN sur data2022HALF2 est : ",int(data2022HALF2.isna().sum()))
    #
    ## 
    datafinal=pd.concat([data2019,data2020,data2021,data2022HALF1,data2022HALF2],axis=0)
    return datafinal
# %%

def prediction(energie): 
    """Revoie un dataframe de la prediction de la consommation
    d'energie du 8 decembre 2022 par 15 minutes 
    energie(str):Nom de l'energie dans le dataset
    return dataframe"""

    import warnings
    warnings.filterwarnings('ignore')
    warnings.simplefilter('ignore')
    import numpy as np
    import pandas as pd
    #plotting
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()
    #machine learning et Méthodes statistiques
    import statsmodels.api as sm

    #Désactiver les avertissements inutiles si nécessaire
    import warnings

    # importation de base des donneés de 2019-01-01 00:00:00 à 2022-11-29 12:45:00 
    import CreationData as cr
    df = cr.dataframe('Consommation (MW)')

    ## Diviser les données en data test et data train 
    data_test = df.iloc[-35880:,:].copy() # 20%
    data_train = df.iloc[:-35880].copy()  # 80%

    # Unobserved Components model definition
    model_UC1 = sm.tsa.UnobservedComponents(df,
                                            level='dtrend',
                                            irregular=True,
                                            stochastic_level = False,
                                            stochastic_trend = False,
                                            stochastic_freq_seasonal = [False, False, False],
                                            freq_seasonal=[{'period': 672, 'harmonics': 1},
                                                        {'period': 2880, 'harmonics': 1},
                                                        {'period': 35066, 'harmonics': 2}])

    # essayage du modèle aux données du train data
    model_UC1res = model_UC1.fit()

    #modèle de prédiction 
    forecast_UC1 = model_UC1res.forecast(steps=35880)

    #calculating mean absolute error and root mean squared error for out-of-sample prediction for model evaluation
    error = np.sqrt(np.mean([(data_test.iloc[x,:] - forecast_UC1[x]) ** 2 for x in range(len(forecast_UC1))]))      
    print(f"Out-of-sample root mean squared error (RMSE): {'%.0f' % error}")

    # Tracé les diagnostics résiduels du modèle Unobserved Components
    model_UC1res.plot_diagnostics(figsize=(18,18),lags=60).set_dpi(200);

    pred = model_UC1res.predict(start="2019-01-01 06:00:00", end="2022-12-08 23:45:00")
    f = plt.figure(figsize=(18,6),dpi=200);

    #la prédiction du jour 8 décembre 2022
    forcast = model_UC1res.predict(start="2022-12-08 00:00:00", end="2022-12-08 23:45:00")
    forcast = forcast.to_frame()
    forcast.rename(columns = {'predicted_mean':energie },inplace = True)
    pd.options.display.max_rows = None
    return forcast


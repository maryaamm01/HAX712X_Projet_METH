#%%
import CreationData as cr
#mathematical operations
import numpy as np

#plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#machine learning and statistical methods
import statsmodels.api as sm

#muting unnecessary warnings if needed
import warnings
# %%____________________________________________-
df = cr.dataframe() # data from 2019-01-01 00:00:00 to 2022-11-29 12:45:00

# %%
#splitting time series to train and test subsets
data_test = ts.iloc[-35880:,:].copy()
#Unobserved Components model definition

 model_UC1= sm.tsa.UnobservedComponents(df,
                                        level='dtrend',
                                        irregular=True,
                                        stochastic_level = False,
                                        stochastic_trend = False,
                                        stochastic_freq_seasonal = [True, False, False],
                                        freq_seasonal=[{'period': 96, 'harmonics': 6},
                                                       {'period': 672, 'harmonics': 2},
                                                       {'period': 35066, 'harmonics': 1}])
#fitting model to train data
model_UC1res = model_UC1.fit()

#printing statsmodels summary for model
print(model_UC1res.summary())


#calculating mean absolute error and root mean squared error for in-sample prediction of model
print(f"In-sample mean absolute error (MAE): {'%.0f' % model_UC1res.mae}, In-sample root mean squared error (RMSE): {'%.0f' % np.sqrt(model_UC1res.mse)}")

#model forecast
forecast_UC1 = model_UC1res.forecast(steps=35880)

#calculating mean absolute error and root mean squared error for out-of-sample prediction for model evaluation
error = np.sqrt(np.mean([(data_test.iloc[x,:] - forecast_UC1[x]) ** 2 for x in range(len(forecast_UC1))]))      
print(f"Out-of-sample root mean squared error (RMSE): {'%.0f' % error}")
# %%__________________
#plotting residual diagnostics of Unobserved Components model
model_UC1res.plot_diagnostics(figsize=(18,18),lags=60).set_dpi(200);
plt.show();
# %%
forc= model_UC1res.predict(start="2022-12-08 00:00:00", end="2022-12-08 23:45:00")
forc.plot()
# %%

pred = model_UC1res.predict(start="2019-01-01 06:00:00", end="2022-12-08 23:45:00")
f = plt.figure(figsize=(18,6),dpi=200);
#setting title and size of title
plt.suptitle('Unobserved Components model prediction Vs Real dataset', fontsize=20);
#setting y axis label
plt.ylabel('MW');
#plotting trend component
plt.plot(df, label='France Electric Power Energy consumption (MW)');
#plotting linear model of trend component
plt.plot(pred, label='Unobserved Components model prediction');

plt.legend();
# %%

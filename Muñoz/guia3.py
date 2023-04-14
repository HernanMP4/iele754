

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import poisson
from scipy.optimize import curve_fit
from scipy.stats
import numpy as np
import powerlaw as pl


#%%
URL = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv'
data = pd.read_csv(URL)
#%%
vals = list(data.columns)[5:-1]
ids = list(data.columns)[0:5]
df_cases_tidy = pd.melt(data, value_vars=vals, id_vars=ids)

#%%
#a)limpiamos fechas
df_cases_tidy['fecha'] = pd.to_datetime(df_cases_tidy['variable'])

# Definir las fechas de inicio y fin
fi= '2020-03-01'
ff= '2020-05-10'
# %%
df_cases_month = df_cases_tidy[(df_cases_tidy['fecha'] >= fi) & (df_cases_tidy['fecha'] <= ff)]

# %%
df_case_sn = df_cases_month.dropna()
#ordenando por valores de fechas el df
df=df_case_sn.sort_values('fecha')
#cambiamos a tipo str value (dice que es el error, vamos a probar)

#%%
df_grouped= df.groupby(df['fecha'])['value'].sum().reset_index()
df_grouped["new_cases"] = df_grouped["value"].diff()

#%%
sns.lineplot(x='fecha',y='new_cases',data=df_grouped)


















# %%
#mu = stats.poisson.f(df_grouped['new_cases'].dropna())
# Define the Poisson distribution function
def poisson_func(k, lamb):
    return poisson.pmf(k, lamb)

# Use curve_fit to fit the data to the Poisson distribution function
params, cov = curve_fit(poisson_func, np.arange(len(data)), data)
# Ajuste de la curva powerlaw

fit = pl.Fit(df_grouped['new_cases'])
alpha = fit.alpha
xmin = fit.xmin

print("Parámetros de ajuste para la curva Poisson: mu =", mu)
print("Parámetros de ajuste para la curva powerlaw: alpha =", alpha, "xmin =", xmin)

#%%
plt.hist(df_grouped['value'], bins=50, density=True)

[mean_fit, std_fit] = stats.norm.fit(df_grouped['value'])

print(mean_fit)
print(std_fit)

x = np.linspace(np.min(df_grouped['value']), np.max(df_grouped['value']))

plt.plot(x, stats.norm.pdf(x, mean_fit, std_fit),)

plt.show()
# %%


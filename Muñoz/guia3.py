

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np
from scipy.stats import powerlaw

#%%
URL = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv'

data = pd.read_csv(URL)
#%%
vals = list(data.columns)[5:-1]
ids = list(data.columns)[:5]
df_cases_tidy = pd.melt(data, value_vars=vals, id_vars=ids)

#%%
df_cases_tidy= df_cases_tidy.rename(columns={'variable':'fecha'})
#a)limpiamos fechas
df_cases_tidy['fecha'] = pd.to_datetime(df_cases_tidy['fecha'], format='%d-%m-%Y')
df_cases_sn = df_cases_tidy.dropna()

# %%
# Definir las fechas de inicio y fin
fi= '2020-03-01'
ff= '2020-05-10'
df_cases_month = df_cases_sn[(df_cases_sn['fecha'] >= fi) & (df_cases_sn['fecha'] <= ff)]

#%%
df_grouped= df_cases_month.groupby(df_cases_month['fecha'])['value'].sum().reset_index()
df_grouped["new_cases"] = df_grouped["value"].diff().fillna(df_grouped["value"])

#%%
print(df_grouped['value'].describe())

#%%
params = powerlaw.fit(df_grouped['value'])
print(params)
fig, ax = plt.subplots()
ax.plot(params, color='red')
#ax.scatter(df_grouped['fecha'], df_grouped['value'], label='Datos')
#%%
# Trazar histograma de los datos
plt.scatter(df_grouped['fecha'], df_grouped['value'], label='Datos')
#plt.hist(df_grouped['fecha'], powerlaw.pdf(df_grouped['value'], *params), label='Ajuste')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# %%
##############OTRA FORMA

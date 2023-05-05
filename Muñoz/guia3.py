

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
print(df_grouped['new_cases'].describe())

#para visualizar 
plt.hist(df_grouped['value'], bins=20)
plt.xlabel('Valores de mi_columna')
plt.ylabel('Frecuencia')
plt.show()

#%%
sns.lineplot(x='fecha',y='new_cases',data=df_grouped)

#%%
fit = powerlaw.fit(df_grouped['new_cases'])
exponent = fit[0]

#%%
# Trazar histograma de los datos
plt.hist(df_grouped['new_cases'], bins=50, density=True)

# Ajustar una curva de densidad de probabilidad a la distribución
fit = powerlaw.Fit(df_grouped['new_cases'])

# Imprimir los parámetros ajustados de la distribución powerlaw
print("alpha = ", fit.alpha)
print("xmin = ", fit.xmin)

# Trazar la curva de densidad de probabilidad ajustada en la parte superior del histograma
x = np.linspace(np.min(df_grouped['new_cases']), np.max(df_grouped['new_cases']), 100)
y = fit.pdf(x)
plt.plot(x, y, 'r--', linewidth=2)

# Mostrar el gráfico
plt.show()

# %%

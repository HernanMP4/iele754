

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np
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
ff= '2020-05-31'
# %%
df_cases_month = df_cases_tidy[(df_cases_tidy['fecha'] >= fi) & (df_cases_tidy['fecha'] <= ff)]

# %%
df_case_sn = df_cases_month.dropna()
#ordenando por valores de fechas el df
df=df_case_sn.sort_values('fecha')
#cambiamos a tipo str value (dice que es el error, vamos a probar)

# %%
plt.hist(df['value'], bins=50, density=True)

[mean_fit, std_fit] = stats.poisson.fit(df['value'])

print(mean_fit)
print(std_fit)

x = np.linspace(np.min(df['value']), np.max(df['value']))

plt.plot(x, stats.norm.pdf(x, mean_fit, std_fit),)

plt.show()
# %%


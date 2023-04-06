#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
#%%
URL = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv'

data = pd.read_csv(URL)

#%%
vals = list(data.columns)[5:-1]
ids = list(data.columns)[0:5]
df_cases_tidy = pd.melt(data, value_vars=vals, id_vars=ids)

#%%
#a)limpiamos fechas
df_cases_tidy['variable'] = pd.to_datetime(df_cases_tidy['variable'])

# Definir las fechas de inicio y fin
fi= '2020-04-13'
ff= '2020-05-10'
                                             
# Filtrar el conjunto de datos para mantener solo las filas entre las fechas de inicio y fin
df_cases_month = df_cases_tidy[(df_cases_tidy['variable'] >= fi) & (df_cases_tidy['variable'] <= ff)]

#%%
# Mostrar el resultado



# eliminamos datos nulos
df_case_sn = df_cases_month.dropna()


df_case_sn['variable'] = pd.to_datetime(df_case_sn['variable'])
df_case_sn['value'] = pd.to_numeric(df_case_sn['value'])

df=df_case_sn.sort_values(by='variable')


# cambiar nombre a columna de fechas
df = df.rename(columns={'variable': 'fechas'})
#df['case_tot']=df['value'].cumsum()

#%% 

df_arica=df[df['Comuna']=='Arica'] 
df_arica['dif']=df_arica['value'].diff()

plt.plot(df_arica['fechas'], df_arica['dif'])
plt.show()

#por lo tanto se concluye que la evolucion del virus es de forma exponencial (nos dimos cuenta de esto ravisando los datos dentro de las fechas con diferencia negativa)
# %%                    
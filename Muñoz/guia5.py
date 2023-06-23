
#%%
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
#%%
Ruta= 'last_uci.xlsx'

df = pd.read_excel(Ruta)
# %%
df.head()

#%%
#"transponemos df", por orden de filas
df_tidy = df.transpose()  # Transponer el dataframe

# Establecer los nombres de las columnas como los valores de la primera fila
df_tidy.columns = df_tidy.iloc[0]

# Eliminar la primera fila, que ahora son los nombres de las columnas duplicados
df_tidy = df_tidy[1:]

df_transposed = df_tidy.reset_index(drop=False)  # Reiniciar los índices de fila y eliminar el índice original

df_tidy= df_transposed.rename(columns={'index':'fecha'})

#%%
#verificamos si hay valores faltantes
##en general
df_tidy.isnull().sum()
#%%
##por formalidad verificamos en 'Total'
df_tidy['Total'].isnull().any()
###No existen valores faltantes

# %%
df_tidy['fecha']=pd.to_datetime(df_cases_tidy['fecha'], format='%d-%m-%Y')

# %%
valor_medio=df_tidy['Total'].mean()
# %%
plt.hist(df_tidy['Total'])
plt.show()
# %%
df_tidy['Total '] = df_tidy['Total'].astype(float)
#%%
##calculamos correlacion entre 2 columnas
correlacion= df_tidy['Total'].corr(df_tidy['Región Metropolitana de Santiago '])
# %%
df_tidy.plot(x='fecha',y='Total')
plt.show()
# %%
# Descompone una columna de series temporales
descomposicion = seasonal_decompose(df_tidy['Total'],
                                    model='additive', period=1)
descomposicion.plot()
plt.show()
# %%
#crear modelo ARIMA
df_tidy['Total'] = df_tidy['Total'].astype(float)  # Convertir la columna a tipo float

# Ajustar el modelo ARIMA
modelo = ARIMA(df_tidy['Total'], order=(5, 1, 0))
modelo_ajustado = modelo.fit()
# %%
prediccion = modelo_ajustado.forecast(steps=10)

print(prediccion)
# %%

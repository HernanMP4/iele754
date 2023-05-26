
#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

#%%
url = "https://raw.githubusercontent.com/rociochavezmx/Rocio-Chavez-youtube-Files/master/Contaminacion%20Atmosferica.csv"
df= pd.read_csv(url)
# %%
#orrelacion entre Velocidad_viento y lluvia
v1 = 'Habitantes'
v2 = 'Lluvia'

correlation = df[v1].corr(df[v2])
print("Correlación entre", v1, "y", v2, ":", correlation)

print(df.columns)

plt.matshow(df.corr())
plt.colorbar()
plt.show()

# %%
#regresion lineal 
###modelo de regresión lineal
model = LinearRegression()
model.fit(df[[v1]] , df[v2])

###coeficientes de la regresion
coeficiente = model.coef_[0]
intercepto = model.intercept_

###Calcular los valores predichos
y_pred = model.predict(df[[v1]] )

###Graficar los resultados
plt.scatter(df[[v1]] , df[v2], color='blue', label='Datos reales')
plt.plot(df[[v1]] , y_pred, color='red', label='Regresión lineal')
plt.xlabel(v1)
plt.ylabel(v2)
plt.title('RL')
plt.legend()
plt.show()

# %%
corr, p_value = pearsonr(df[v1], df[v2])
print("Correlation: ", corr)
print("P-value: ", p_value)
# %%

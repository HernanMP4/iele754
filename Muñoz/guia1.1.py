 #pip install scipy

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

URL2023 = 'https://raw.githubusercontent.com/MinCiencia/Datos-CambioClimatico/main/output/temperatura_aire_ceaza/2023/2023_temperatura_aire_ceaza.csv'
URL2020 = 'https://raw.githubusercontent.com/MinCiencia/Datos-CambioClimatico/main/output/temperatura_aire_ceaza/2020/2020_temperatura_aire_ceaza.csv'

data2023 = pd.read_csv(URL2023)
print(data2023)
data2023.head()

data2020 = pd.read_csv(URL2020)
data2020.head()

dt2023 = pd.DataFrame(data2023)
dt2020 = pd.DataFrame(data2020)

#TRABAJAMOS 2023
dt2023.info()
## pasamos a time a fecha
dt2023['time'] = pd.DatetimeIndex(dt2023['time']).month
dt2023
## filtramos mes 
dtmes2023=dt2023.loc[dt2023['time']==2] #abril no tiene data
dtmes2023
dtmes2023.info()

#TRABAJAMOS 2020
dt2020.info()
## pasamos a time a fecha
dt2020['time'] = pd.DatetimeIndex(dt2020['time']).month
dt2020
## filtramos mes 
dtmes2020=dt2020.loc[dt2020['time']==2]
dtmes2020

#GRAFICOS
sns.kdeplot(data=dtmes2023 , x="prom", label="2023")
sns.kdeplot(data=dtmes2020 , x="prom", label="2020")

#poniendolo bonito
plt.xlabel('T°')
plt.ylabel('Probabilidad')

#viendo si la diferencia es significante
##Realizar la prueba ANOVA
fvalue, pvalue = stats.f_oneway(dtmes2020['prom'], dtmes2023['prom'])

##Imprimir el valor p
print('Valor p:', pvalue)

##Interpretar el resultado
if pvalue < 0.05:
    print('Existe una diferencia significativa entre las muestras')
else:
    print('No existe una diferencia significativa entre las muestras')
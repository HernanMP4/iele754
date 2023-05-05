#%%
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from scipy.stats import bernoulli,norm
#%%
#aka missing completly at random
N = 100 #Estos 3 usan el signo "<-" en vez del "=
S = norm(0,1).rvs(size=N)
H = norm(0,0.5*S).rvs(size=N)
sns.scatterplot(data=S)
sns.scatterplot(data=H)
#%%

D = np.random.binomial(n=1, p=0.85, size=N) #D = rbern(N,8.5)
Hstar = H.copy()
Hstar[D==1] = np.nan

plt.plot(S, H, c="gray", alpha=0.8, linewidth=2)
plt.scatter(S, Hstar, c="red", linewidth=3)  #col=2
plt.show()  
 
 #%%
 #Perro se come la tarea random
#NONELINEAR WITH CEILING EFFECT
N = 100 
S = np.random.normal(size=N)  
H = np.random.normal(loc=0, scale=(1-(np.exp(-0.7*S))), size=N )
 
#El perro se come el 100% de la tarea con S>0
D = np.random.binomial(n=1, p=np.where(S > 0, 1, 0), size=N)

Hstar = H.copy()
Hstar[D==1] = np.nan 

plt.plot(S, H, c="gray", alpha=0.8, linewidth=2) 
plt.scatter(S, Hstar, c="red", linewidth=3)  #col=2
plt.show()  

#%%
# Perro se come la tarea random
# NONELINEAR WITH CEILING EFFECT
N = 100
S = np.random.normal(size=N)
H = np.random.normal(loc=0, scale=np.sqrt(1 - 0.7*S**2), size=N)

# El perro se come el 100% de la tarea con S > 0
D = np.random.binomial(n=1, p=np.where(S > 0, 1, 0), size=N)
Hstar = H.copy()
Hstar[D==1] = np.nan 

plt.plot(S, H, c="gray", alpha=0.8, linewidth=2) 
plt.scatter(S, Hstar, c="red", linewidth=3)  #col=2
plt.show()  
# %%
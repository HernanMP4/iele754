

#%%
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from scipy.stats import bernoulli,norm
#%%
N = 100
S = np.random.normal(size=N)
H = np.random.normal(0.5*S, size=N)
# dog eats 50% of homework at random
D = np.random.binomial(1, 0.5, size=N) 
Hstar = H.copy()
Hstar[D==1] = np.nan

plt.plot(S , H , color='gray', linewidth=2 )
plt.scatter(S , Hstar , color='red' , s=50 , linewidth=3 )

plt.plot(S, np.polyval(np.polyfit(S, H, deg=1), S), color='gray', linewidth=3)
plt.plot(S, np.polyval(np.polyfit(S[~np.isnan(Hstar)], Hstar[~np.isnan(Hstar)], deg=1), S), color='red', linewidth=3)

plt.show()

#%%
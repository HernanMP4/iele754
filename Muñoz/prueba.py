#%%
import scipy.stats as stats#aqui estan las distribuicones: uniform, norm, binom, geom, poisson
ud=stats.uniform.rvs(size=100000,loc=0,scale=10)
# %%
import random
# %%
random.random()
# %%
random.randint(0,10)
random.choice([2,4,6,8,9])
# %%    
random.seed(19)#set the seed to the same values in the randoms
print([random.uniform(0,10) for x in range(4)])
# %%
 
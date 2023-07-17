import random
import numpy as np
import matplotlib.pyplot as plt

def arrival_rate_back_to_city():
    plt.cla()
    random.seed(1)
    mu, var, samples = 9, 2, 30
    sample_pop = np.random.normal(mu, var, samples)
    sample_pop.sort()
    even_index = list(range(0, sample_pop.size, 2))
    odd_index = list(range(1, sample_pop.size, 2))
    odd_index.reverse()
    index = even_index + odd_index
    # samples of pop according to gaussian normal distribution
    samples = sample_pop[index]
    return samples

def departure_rate_for_hoilday():
    plt.cla()
    random.seed(1)
    mu, var, samples = 12.5, 2.3, 30
    sample_pop = np.random.normal(mu, var, samples)
    sample_pop.sort()
    even_index = list(range(0, sample_pop.size, 2))
    odd_index = list(range(1, sample_pop.size, 2))
    odd_index.reverse()
    index = even_index + odd_index
    # samples of pop according to gaussian normal distribution
    samples = sample_pop[index]
    return samples

df1 = departure_rate_for_hoilday()
df2= arrival_rate_back_to_city()
plt.plot(df1, label='departure_rate')
plt.plot(df2,label='arrival_rate')
plt.xlabel(' Day of a month')
plt.ylabel(' Fraction of population leaving and coming back to city')
plt.legend(loc='best')
plt.savefig('dep_arrival_rate1.png')
plt.show()


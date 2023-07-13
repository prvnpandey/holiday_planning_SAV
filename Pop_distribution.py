import random
import numpy as np
import matplotlib.pyplot as plt

for i in range(0,1):
    plt.cla()
    random.seed(1)
    mu, var, samples = 12, 2.3, 30
    sample_pop = np.random.normal(mu, var, samples)
    sample_pop.sort()
    even_index = list(range(0, sample_pop.size, 2))
    odd_index = list(range(1, sample_pop.size, 2))
    odd_index.reverse()
    index = even_index + odd_index
    # samples of pop according to gaussian normal distribution
    samples = sample_pop[index]

    plt.plot(samples)
    plt.show()

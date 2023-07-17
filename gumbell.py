import numpy as np
import matplotlib.pyplot as plt

def gumbell_distribution():
    mu, beta = 1.0, 4.5# location and scale

    s = np.random.gumbel(mu, beta, 30)

    means = []

    maxima = []

    for i in range(0,1000) :

       a = np.random.normal(mu, beta, 30)

       means.append(a.mean())

       maxima.append(a.max())

    count, bins, ignored = plt.hist(maxima, 30, density=True)

    beta = np.std(maxima) * np.sqrt(6) / np.pi

    mu = np.mean(maxima) - 0.57721*beta

    arrival_rate = (1/beta)*np.exp(-(bins - mu)/beta) * np.exp(-np.exp(-(bins - mu)/beta))
    dep_rate = 1/(beta * np.sqrt(2 * np.pi))* np.exp(-(bins - mu)**2 / (2 * beta**2))

    # plt.plot(arrival_rate,linewidth=2, color='r', label='arrival_rate')
    #
    # plt.plot(dep_rate,linewidth=2, color='g', label = 'dep_rate')
    # plt.legend()
    # plt.show()
    return dep_rate, arrival_rate
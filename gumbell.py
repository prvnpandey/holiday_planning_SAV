import numpy as np
import matplotlib.pyplot as plt

def gumbell_distribution(samplesize):
    mu, beta = 1.0, 4.5# location and scale
    # mu, beta = 0.9, 5
    period = 30

    s = np.random.gumbel(mu, beta, period)
    means = []
    maxima = []
    for i in range(0,1000) :

       a = np.random.normal(mu, beta, period)

       means.append(a.mean())

       maxima.append(a.max())

    count, bins, ignored = plt.hist(maxima, period, density=True)
    plt.cla()

    beta = np.std(maxima) * np.sqrt(6) / np.pi

    mu = np.mean(maxima) - 0.57721*beta

    arrival_rate = (1/beta)*np.exp(-(bins - mu)/beta) * np.exp(-np.exp(-(bins - mu)/beta))
    dep_rate = 1/(beta * np.sqrt(2 * np.pi))* np.exp(-(bins - mu)**2 / (2 * beta**2))
    dep_rate =samplesize * (dep_rate/dep_rate.sum())
    # dep_rate = dep_rate* (samplesize/dep_rate.max())
    arrival_rate = samplesize * (arrival_rate / arrival_rate.sum())
    # arrival_rate = arrival_rate * (samplesize / arrival_rate.max())
    # adding few starting days with no return rate back to city
    arrival_rate = np.insert(arrival_rate, [0,1,2], [0,0,0])

    return dep_rate, arrival_rate


import matplotlib.pyplot as plt
import numpy as np


def plot_graph(arrival_rate, dep_rate):
    plt.plot(arrival_rate,linewidth=2, color='r', label='arrival_rate')

    plt.plot(dep_rate,linewidth=2, color='g', label = 'dep_rate')
    plt.legend()
    plt.title('The percentage of population leaving and coming back to city for each day')
    plt.xlabel('Caldender Days')
    plt.ylabel('Percentage of population')
    return plt.show()
def plot_cdf(arrival_rate, dep_rate):
    plt.plot(np.cumsum(arrival_rate),linewidth=2, color='r', label='arrival_rate')

    plt.plot(np.cumsum(dep_rate),linewidth=2, color='g', label = 'dep_rate')
    plt.legend()
    plt.title('CDF plot of arrival and departure rate')
    plt.xlabel('Caldender Days')
    plt.ylabel('Percentage of population')
    return plt.show()

def scenario1_graph(additinal_fleet, city_pop, RoundTriptime, PERCENTAGE):
    fig,(ax1,ax2) = plt.subplots(2, sharex=True)
    ax2.plot(city_pop,linewidth=2, color='r', label = 'city population per day')
    ax1.plot(additinal_fleet, linewidth=2, color='r', label='Round Trip time = ' + str(RoundTriptime) + ' day ' )
    ax1.set_ylabel('additional SAV')
    ax2.set_ylabel('Number of people')
    plt.xlabel('Caldender Days')
    fig.set_tight_layout(True)
    fig.suptitle('The additial fleet and city population over the days \nwith a cummulative hoilday trips with '  +str(PERCENTAGE) + ' %')
    plt.legend()
    plt.savefig(f'figures/Scenario_{PERCENTAGE}_{RoundTriptime}.png', dpi=600)
    return plt.show()
def scenario_graph(*args , **kwargs):
    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    ax2.plot(args[1], linewidth=2, color='r', label='vehicle back to city')
    ax1.plot(args[0], linewidth=2, color='r', label='Round Trip time = ' + str(kwargs.get('RoundTriptime')) + ' day')
    ax1.set_ylabel('Fleet required by hoilday \n fleet operator')
    ax2.set_ylabel('Number of people \n per day in city')
    plt.xlabel('Caldender Days')
    fig.suptitle('SAV fleet and city population over the days (Scenario 2)')
    fig.set_tight_layout(True)
    # plt.legend(loc='right')
    return plt.show()
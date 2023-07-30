import matplotlib.pyplot as plt
def plot_graph(arrival_rate, dep_rate):
    plt.plot(arrival_rate,linewidth=2, color='r', label='arrival_rate')

    plt.plot(dep_rate,linewidth=2, color='g', label = 'dep_rate')
    plt.legend()
    plt.title('The percentage of population leaving and coming back to city for each day')
    plt.xlabel('Caldender Days')
    plt.ylabel('Percentage of population')
    return plt.show()

def scenario1_graph(additinal_fleet, city_pop):
    fig,(ax1,ax2) = plt.subplots(2, sharex=True)
    ax1.plot(additinal_fleet,linewidth=2, color='r', label='additinal_fleet per day')
    ax2.plot(city_pop,linewidth=2, color='r', label = 'city population per day')
    ax1.set_ylabel('additional SAV')
    ax2.set_ylabel('Number of people')
    plt.xlabel('Caldender Days')
    fig.suptitle('The additial fleet and city population over the days (Scenario 1)')
    return plt.show()
def scenario_graph(*args, **kwargs):
    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    ax1.plot(args[0], linewidth=2, color='r', label='additinal_fleet per day')
    ax2.plot(args[1], linewidth=2, color='r', label='vehicle back to city')
    ax1.set_ylabel('Outside trip fleet')
    ax2.set_ylabel('vehicle back to city')
    plt.xlabel('Caldender Days')
    fig.suptitle('The additial fleet and vehicle back to city over the days (Scenario 2)')
    return plt.show()
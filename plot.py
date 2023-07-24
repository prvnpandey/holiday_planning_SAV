import matplotlib.pyplot as plt
def plot_graph(arrival_rate, dep_rate):
    plt.plot(arrival_rate,linewidth=2, color='r', label='arrival_rate')

    plt.plot(dep_rate,linewidth=2, color='g', label = 'dep_rate')
    plt.legend()
    plt.title('The percentage of population leaving and coming back to city for each day')
    plt.xlabel('Caldender Days')
    plt.ylabel('Percentage of population')
    return plt.show()
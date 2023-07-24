
import Pop_distribution
import gumbell
import plot
from scenario import scenario_2, scenario_1
from print_result import scenario_2_result, scenario_1_result
# import simpy

class initial_scenario():
    def __init__(self, population, fleet, passenger_per_vehicle):
        self.population = population
        self.fleet = fleet
        self.passenger_per_vehicle = passenger_per_vehicle

if __name__ == '__main__':
    #population = int(input('enter the population in city, must be an integer value'))
    population = 1000
    # the percent of total population went on vacation on in a month
    percent_of_population_on_hoilday = 0.2
    scenario = initial_scenario(population, population*0.1, 2 )
    dep_rate, arrival_rate = gumbell.gumbell_distribution(samplesize= percent_of_population_on_hoilday)
    plot.plot_graph(arrival_rate, dep_rate)
    fleet, population, hoilday, hoilday_fleet,additional_fleet_per_day = scenario_1(scenario, dep_rate, arrival_rate)
    scenario_1_result(scenario, fleet, population, hoilday, hoilday_fleet)
 #___________________________________Scenario_2________________________________________________________________________

    Net_vehcile_required_for_outside_trips = scenario_2(scenario,dep_rate, arrival_rate)
    scenario_2_result(scenario, Net_vehcile_required_for_outside_trips)











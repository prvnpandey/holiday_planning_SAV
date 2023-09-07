import random

import Pop_distribution
import gumbell
import plot
from scenario import scenario_1, scenario_2, scenario_3
import matplotlib.pyplot as plt
from print_result import scenario_2_result, scenario_1_result
# import simpy

class Initialization():
    def __init__(self, population, fleet, passenger_per_vehicle):
        self.population = population
        self.fleet = fleet
        self.passenger_per_vehicle = passenger_per_vehicle
    def vehicle_maintence(self):
        return round(random.uniform(0,5),3)/100

if __name__ == '__main__':
    #population = int(input('enter the population in city, must be an integer value'))
    population = 1000
    RoundTripTime = 0
    # the percent of total population went on vacation on in a month
    percent_of_population_on_hoilday = 0.2
    scenario = Initialization(population, population*0.1, 2 )
    dep_rate, arrival_rate = gumbell.gumbell_distribution(samplesize= percent_of_population_on_hoilday)
    # plot.plot_graph(arrival_rate, dep_rate)
    # plot.plot_cdf(arrival_rate, dep_rate)
    # fleet, population, hoilday, hoilday_fleet,additional_fleet_per_day = scenario_1(scenario, dep_rate, arrival_rate)
    fleet, city_pop = scenario_1(scenario, dep_rate, arrival_rate, RoundTripTime)
    plot.scenario1_graph(fleet, city_pop, RoundTripTime)

 #    scenario_1_result(scenario, fleet, population, hoilday, hoilday_fleet)
 # #___________________________________Scenario_2________________________________________________________________________
 #
    Net_vehcile_required, veh_in = scenario_2(scenario,dep_rate, arrival_rate, RoundTripTime)
    # plot.scenario1_graph(net_veh=Net_vehcile_required, veh_in=veh_in)
    plot.scenario_graph(Net_vehcile_required, veh_in , RoundTriptime=RoundTripTime)
    # scenario_2_result(scenario, Net_vehcile_required_for_outside_trips)

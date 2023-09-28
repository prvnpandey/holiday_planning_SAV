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
    POPULATION = [100000]
    ROUNDTRIPTIME = 2
    PERCENTAGE = 0.3
    dep_rate, arrival_rate = gumbell.gumbell_distribution(PERCENTAGE, ROUNDTRIPTIME)
    for population in POPULATION:
        # the percent of total population went on vacation on in a month
        scenario = Initialization(population, population*0.1, 2 )
        # plot.plot_graph(arrival_rate, dep_rate)
        # plot.plot_cdf(arrival_rate, dep_rate)
        # fleet, population, hoilday, hoilday_fleet,additional_fleet_per_day = scenario_1(scenario, dep_rate, arrival_rate)
        fleet, city_pop = scenario_1(scenario, dep_rate, arrival_rate, ROUNDTRIPTIME)
        plot.scenario1_graph(fleet, city_pop, ROUNDTRIPTIME, PERCENTAGE)

     #    scenario_1_result(scenario, fleet, population, hoilday, hoilday_fleet)

     # #___________________________________Scenario_2________________________________________________________________________
     #    Net_vehcile_required, veh_in = scenario_2(scenario,dep_rate, arrival_rate, ROUNDTRIPTIME)
     #    # plot.scenario1_graph(net_veh=Net_vehcile_required, veh_in=veh_in)
     #    plot.scenario_graph(Net_vehcile_required, veh_in , RoundTriptime=ROUNDTRIPTIME)
     #    # scenario_2_result(scenario, Net_vehcile_required)

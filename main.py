import random
from xlrd import book

import Pop_distribution
import gumbell

import plot
from scenario import scenario_1, scenario_2, scenario_3
import matplotlib.pyplot as plt
import pandas as pd
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
<<<<<<<<< Temporary merge branch 1
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
=========
    from openpyxl import load_workbook
    POPULATION = 100000
    ROUNDTRIPTIME = [0,1,2,3,4,5]
    PERCENTAGE = [0.2, 0.3, 0.4, 0.5]
    workbook_name = 'simulation_test.xlsx'
    wb = load_workbook(workbook_name)
    writer = pd.ExcelWriter(wb, engine='openpyxl')
    writer.book = book
    sheet_name = 'Sheet1'
    df = pd.read_excel(wb, sheet_name=sheet_name,engine='openpyxl')


    # the percent of total population went on vacation on in a month
    for roundtrip in ROUNDTRIPTIME:
        for percentage in PERCENTAGE:
            dep_rate, arrival_rate = gumbell.gumbell_distribution(percentage, roundtrip)
            scenario = Initialization(POPULATION, POPULATION*0.1, 2 )
            # plot.plot_graph(arrival_rate, dep_rate)
            # plot.plot_cdf(arrival_rate, dep_rate)
            # fleet, population, hoilday, hoilday_fleet,additional_fleet_per_day = scenario_1(scenario, dep_rate, arrival_rate)
            fleet, city_pop = scenario_1(scenario, dep_rate, arrival_rate, roundtrip)
            # plot.scenario1_graph(fleet, city_pop, ROUNDTRIPTIME, PERCENTAGE)
            # calculate statistics
            stats = {'Population':POPULATION,'RoundTripTime':roundtrip,
                     'percent_of_pop_at_hoilday':percentage,
                     'fleet_per_passenger':POPULATION/(POPULATION/10),
                     'additinlal_fleet':max(fleet),
                     'fleet_per_passenger_after_simulation':POPULATION/(POPULATION/10+max(fleet)),
                     'increased_fleet_in(%)':((POPULATION/(POPULATION/10)) - (POPULATION/(POPULATION/10+max(fleet))))/ (POPULATION/(POPULATION/10))*100}
            new_df = pd.DataFrame(stats, index=[0])
            df = df.append(new_df, ignore_index=True)
            df.to_excel(workbook_name, sheet_name=sheet_name)
 #    scenario_1_result(scenario, fleet, population, hoilday, hoilday_fleet)
>>>>>>>>> Temporary merge branch 2

     # #___________________________________Scenario_2________________________________________________________________________
     #    Net_vehcile_required, veh_in = scenario_2(scenario,dep_rate, arrival_rate, ROUNDTRIPTIME)
     #    # plot.scenario1_graph(net_veh=Net_vehcile_required, veh_in=veh_in)
     #    plot.scenario_graph(Net_vehcile_required, veh_in , RoundTriptime=ROUNDTRIPTIME)
     #    # scenario_2_result(scenario, Net_vehcile_required)

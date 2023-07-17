import matplotlib.pyplot as plt

from Pop_distribution import arrival_rate_back_to_city, departure_rate_for_hoilday
from gumbell import gumbell_distribution
# import simpy

class initial_scenario():
    def __init__(self, population, fleet, passenger_per_vehicle):
        self.population = population
        self.fleet = fleet
        self.passenger_per_vehicle = passenger_per_vehicle

def scenario_1(scenario, fraction_of_pop_to_holiday,fraction_of_pop_from_holiday):
    fleet = scenario.fleet
    population = scenario.population
    additional_fleet =[]
    for day in range(0,fraction_of_pop_to_holiday.size):
        pop_on_holidayTrips = round(population*(fraction_of_pop_to_holiday[day]/100))
        if(day>0):
            pop_back_to_city = round(population*(fraction_of_pop_from_holiday[day]/100))
        else:
            pop_back_to_city = 0
        required_fleet_for_hoildayTrips = round((pop_on_holidayTrips-pop_back_to_city)/scenario.passenger_per_vehicle)
        population = population-pop_on_holidayTrips +pop_back_to_city
        fleet = fleet - required_fleet_for_hoildayTrips
        additional_fleet.append(round((population*0.1 - fleet)))
        fleet = fleet + additional_fleet[day]

    return fleet, population, scenario.population-population, (scenario.population-population)/scenario.passenger_per_vehicle, additional_fleet

def plot_gumbell(dep_rate, arrival_rate):
    plt.plot(arrival_rate, linewidth=2, color='r', label='arrival_rate')
    plt.plot(dep_rate,linewidth=2, color='g', label = 'dep_rate')
    plt.legend()
    return plt.show()
if __name__ == '__main__':
    #population = int(input('enter the population in city, must be an integer value'))
    population = 100000
    scenario = initial_scenario(population, population*0.1, 2 )
    fraction_of_pop_to_holiday, fraction_of_pop_from_holiday = gumbell_distribution()
    plot_gumbell(fraction_of_pop_from_holiday, fraction_of_pop_to_holiday)
    # fraction_of_pop_to_holiday = Pop_distribution.departure_rate_for_hoilday() # on daily basis
    # fraction_of_pop_from_holiday = Pop_distribution.arrival_rate_back_to_city()
    fleet, population, hoilday, hoilday_fleet,additional_fleet_per_day = scenario_1(scenario, fraction_of_pop_to_holiday, fraction_of_pop_from_holiday)
    print(f'The Population in city is {population}, with a fleet size of {fleet}')
    print(f'The Population on hoilday is {hoilday}, with a fleet size of {hoilday_fleet}')
    print(f'Total required fleet with hoilday scneario is {fleet+hoilday_fleet}')










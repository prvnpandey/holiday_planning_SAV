import Pop_distribution
import simpy

class initial_scenario():
    def __init__(self, population, fleet, passenger_per_vehicle):
        self.population = population
        self.fleet = fleet
        self.passenger_per_vehicle = passenger_per_vehicle

def scenario_1(scenario, fraction_of_pop_holiday):
    fleet = scenario.fleet
    population = scenario.population
    for daily_fraction in fraction_of_pop_holiday:
        pop_on_holidayTrips = round(population*(daily_fraction/100))
        required_fleet_for_hoildayTrips = round(pop_on_holidayTrips/scenario.passenger_per_vehicle)
        population = population-pop_on_holidayTrips
        fleet = fleet - required_fleet_for_hoildayTrips
        fleet = fleet + round((population*0.1 - fleet))
    return fleet, population, scenario.population-population, (scenario.population-population)/scenario.passenger_per_vehicle


if __name__ == '__main__':
    #population = int(input('enter the population in city, must be an integer value'))
    population = 100000
    scenario = initial_scenario(population, population*0.1, 2 )
    fraction_of_pop_holiday = Pop_distribution.samples # on daily basis
    fleet, population, hoilday, hoilday_fleet = scenario_1(scenario, fraction_of_pop_holiday)
    print(f'The Population in city is {population}, with a fleet size of {fleet}')
    print(f'The Population on hoilday is {hoilday}, with a fleet size of {hoilday_fleet}')
    print(f'Total required fleet with hoilday scneario is {fleet+hoilday_fleet}')












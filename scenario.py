# The scenario in which each city has its seperate transport system, and vehcile used for outside trips are kept seperately
import random
def scenario_1(scenario, fraction_of_pop_to_holiday,fraction_of_pop_from_holiday, RoundTripTime):
    fleet = scenario.fleet
    population = scenario.population
    remaining_city_population = []
    additional_fleet =[]
    people_at_holiday = []
    for day in range(0,fraction_of_pop_to_holiday.size):
        pop_cit_to_hoilday = round(population*(fraction_of_pop_to_holiday[day]))
        if(day>RoundTripTime):
            pop_back_to_city = round(population*(fraction_of_pop_from_holiday[day-RoundTripTime]))
            fleet = round(fleet * (1 - scenario.vehicle_maintence()))  # vehcilce maintence factor
        else:
            pop_back_to_city = 0
        if(pop_cit_to_hoilday>1):
            required_fleet_for_hoildayTrips = round((pop_cit_to_hoilday-pop_back_to_city)/scenario.passenger_per_vehicle)
        else:required_fleet_for_hoildayTrips = round((pop_cit_to_hoilday-pop_back_to_city + 1)/scenario.passenger_per_vehicle)
        population = population-pop_cit_to_hoilday +pop_back_to_city
        remaining_city_population.append(population)
        fleet = fleet - required_fleet_for_hoildayTrips
        if fleet<population*0.1:
            additional_fleet.append(round((population*0.1 - fleet)))
        else: additional_fleet.append(0)
        fleet = fleet + additional_fleet[day]
    # return fleet, population, scenario.population-population, (scenario.population-population)/scenario.passenger_per_vehicle, additional_fleet
    return additional_fleet, remaining_city_population
def scenario_2(scenario, fraction_of_pop_to_holiday,fraction_of_pop_from_holiday, RoundTripTime):
    population = scenario.population
    remaining_city_population = []
    # required fleet to service inside the city calculated according to initial population
    veh_in_city = population*0.1/1- scenario.vehicle_maintence()
    # fleet required to manage outside trips
    vehicle_out =[]
    # vehicle coming back to city
    veh_in =[]
    for day in range(0,fraction_of_pop_to_holiday.size):
        pop_on_holidayTrips = round(population*(fraction_of_pop_to_holiday[day]))
        if(day>RoundTripTime):
            pop_back_to_city = round(population*(fraction_of_pop_from_holiday[day-RoundTripTime]))
        else:
            pop_back_to_city = 0
        if(pop_on_holidayTrips>pop_back_to_city):
            vehicle_out.append((pop_on_holidayTrips-pop_back_to_city)/(scenario.passenger_per_vehicle * (1-scenario.vehicle_maintence())))
        else: vehicle_out.append(0)
        population = population - pop_on_holidayTrips + pop_back_to_city
        remaining_city_population.append(population)
        veh_in.append(pop_back_to_city/(scenario.passenger_per_vehicle * (1-scenario.vehicle_maintence())))

    return vehicle_out, remaining_city_population

def scenario_3(scenario, fraction_of_pop_to_holiday,fraction_of_pop_from_holiday, RoundTripTime):
    pass


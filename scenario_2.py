# The scenario in which each city has its seperate transport system, and vehcile used for outside trips are kept seperately

def scenario_2(scenario, fraction_of_pop_to_holiday,fraction_of_pop_from_holiday):
    population = scenario.population
    # required fleet to service inside the city calculated according to initial population
    veh_inside = population*0.1
    # fleet required to manage outside trips
    Net_vehcile_required =[]
    # vehicle coming back to city
    veh_in =[]
    for day in range(0,fraction_of_pop_to_holiday.size):
        pop_on_holidayTrips = round(population*(fraction_of_pop_to_holiday[day]))
        if(day>1):
            pop_back_to_city = round(population*(fraction_of_pop_from_holiday[day]))
        else:
            pop_back_to_city = 0
        if(pop_on_holidayTrips>pop_back_to_city):
            Net_vehcile_required.append((pop_on_holidayTrips-pop_back_to_city)/scenario.passenger_per_vehicle)
        veh_in.append(pop_back_to_city/scenario.passenger_per_vehicle)


    return max(Net_vehcile_required)
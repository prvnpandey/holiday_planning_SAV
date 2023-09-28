
def scenario_1(scenario, fraction_of_pop_C_H, fraction_of_pop_H_C, roundTripTime):

    population = scenario.population

    for day in range(0,fraction_of_pop_C_H.size):
        Pc = population - population*fraction_of_pop_C_H + population*fraction_of_pop_H_C[day-roundTripTime]
        
    return
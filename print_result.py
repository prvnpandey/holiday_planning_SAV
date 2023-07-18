
def scenario_1_result(scenario, hoilday_fleet, Net_vehcile_required_for_outside_trips):
    statemet1 = print(f'The Population in city is {population}, with a fleet size of {fleet}')
    statemet2 = print(f'The Population on hoilday is {hoilday}, with a fleet size of {hoilday_fleet}')
    statemet3 = print(f'Total required fleet with hoilday scneario is {fleet+hoilday_fleet}')
    return statemet1, statemet2, statemet3

def scenario_2_result(scenario, Net_vehcile_required_for_outside_trips):
    statemet1 = print(f'the fleet size of {Net_vehcile_required_for_outside_trips} is sufficiently large to tackle hoilday trips for scenario_2')
    statemet2 = print(f'total fleet size is --> {scenario.fleet + Net_vehcile_required_for_outside_trips}')
    statemet3 = print(f'The populaton to fleet ratio is considering hoilday case is  ---> {scenario.population / (scenario.fleet + Net_vehcile_required_for_outside_trips)}')
    return statemet1, statemet2, statemet3
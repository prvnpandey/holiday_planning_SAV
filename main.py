import Pop_distribution
import simpy

if __name__ == '__main__':
    population = 1000
    fleet = population*0.1
    passenger_per_vehicle = 2
    fraction_of_pop_holiday = Pop_distribution.samples # on daily basis

    for daily_fraction in fraction_of_pop_holiday:
        pop_on_holidayTrips = round(population*(daily_fraction/100))
        required_fleet_for_hoildayTrips = round(pop_on_holidayTrips/passenger_per_vehicle)
        population = population-pop_on_holidayTrips
        fleet = fleet - required_fleet_for_hoildayTrips
        fleet = fleet + (population*0.1 - fleet)









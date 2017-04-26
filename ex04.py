#type(cars) = int
cars = 100
#type(space_in_a_car) = float
space_in_a_car = 4.0
#type(drivers) = int
drivers = 30
#type(passengers) = int
passengers = 90
#type(cars_not_driven) = int
cars_not_driven = cars - drivers
cars_driven = drivers
#type(carpool_capacity) = float, as space_in_a_car is float
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
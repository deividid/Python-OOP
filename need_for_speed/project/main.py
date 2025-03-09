from need_for_speed.project.vehicle import Vehicle
from need_for_speed.project.car import Car
from need_for_speed.project.family_car import FamilyCar
from need_for_speed.project.sport_car import SportCar
from need_for_speed.project.motorcycle import Motorcycle
from need_for_speed.project.cross_motorcycle import CrossMotorcycle
from need_for_speed.project.race_motorcycle import RaceMotorcycle


vehicle = Vehicle(50, 150)

print(Vehicle.DEFAULT_FUEL_CONSUMPTION)

print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)

print(vehicle.fuel)

print(vehicle.horse_power)

print(vehicle.fuel_consumption)

vehicle.drive(100)

print(vehicle.fuel)

family_car = FamilyCar(150, 150)

family_car.drive(50)

print(family_car.fuel)

family_car.drive(50)

print(family_car.fuel)

print(family_car.__class__.__bases__[0].__name__)
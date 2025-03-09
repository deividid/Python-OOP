from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(50, 100)

    def test_of_init(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_without_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(150)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(8)
        self.assertEqual(40, self.vehicle.fuel)

    def test_of_refuel_over_the_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_of_refuel_with_right_amount(self):
        self.vehicle.drive(16)
        self.vehicle.refuel(10)
        self.assertEqual(40, self.vehicle.fuel)

    def test_of_str_method(self):
        self.assertEqual("The vehicle has 100 horse power with 50 fuel left and 1.25 fuel consumption", self.vehicle.__str__())



if __name__ == "__main__":
    main()
from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self) -> None:
        self.robot = ClimbingRobot("Alpine", "DK", 100, 150)
        self.robot_with_software = ClimbingRobot("Alpine", "DK", 100, 150)
        software = {"capacity_consumption": 10, "memory_consumption": 20, "name": "Linux"}
        self.robot_with_software.installed_software.append(software)

    def test_init(self):
        self.assertEqual("Alpine", self.robot.category)
        self.assertEqual("DK", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(150, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_categoty_setter(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Invalid"

        self.assertEqual(f"Category should be one of {self.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_used_capacity(self):
        self.assertEqual(10, self.robot_with_software.get_used_capacity())

    def test_available_capacity_method(self):
        self.assertEqual(90, self.robot_with_software.get_available_capacity())

    def test_used_memory(self):
        self.assertEqual(20, self.robot_with_software.get_used_memory())

    def test_memory_available(self):
        self.assertEqual(130, self.robot_with_software.get_available_memory())

    def test_of_install_software_successfully(self):
        new_software = {"capacity_consumption": 25, "memory_consumption": 35, "name":  "Windows"}
        self.assertEqual(f"Software '{new_software['name']}' successfully installed on {self.robot.category} part.", self.robot.install_software(new_software))
        self.assertEqual([{"capacity_consumption": 25, "memory_consumption": 35, "name":  "Windows"}], self.robot.installed_software)

    def test_of_install_software_successfully_with_equal_values(self):
        new_software = {"capacity_consumption": 100, "memory_consumption": 150, "name":  "Windows"}
        self.assertEqual(f"Software '{new_software['name']}' successfully installed on {self.robot.category} part.", self.robot.install_software(new_software))
        self.assertEqual([{"capacity_consumption": 100, "memory_consumption": 150, "name":  "Windows"}], self.robot.installed_software)

    def test_of_install_software_unsuccessfully_due_to_capacity(self):
        bad_software = {"name": "Softuni", "capacity_consumption": 200, "memory_consumption": 50}
        self.assertEqual(f"Software '{bad_software['name']}' cannot be installed on {self.robot.category} part.",
                         self.robot.install_software(bad_software))

    def test_of_install_software_unsuccessfully_due_to_memory(self):
        bad_software = {"name": "Softuni", "capacity_consumption": 50, "memory_consumption": 250}
        self.assertEqual(f"Software '{bad_software['name']}' cannot be installed on {self.robot.category} part.",
                         self.robot.install_software(bad_software))

    def test_of_install_software_unsuccessfully_due_to_both(self):
        bad_software = {"name": "Softuni", "capacity_consumption": 250, "memory_consumption": 250}
        self.assertEqual(f"Software '{bad_software['name']}' cannot be installed on {self.robot.category} part.",
                         self.robot.install_software(bad_software))




if __name__ == "__main__":
    main()
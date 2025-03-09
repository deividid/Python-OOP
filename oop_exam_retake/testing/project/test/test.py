from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self) -> None:
        self.kfc = Restaurant("KFC", 100)
        self.first_waiter = {"name": "Bruce", "total_earnings": 30}
        self.second_waiter = {"name": "Willis", "total_earnings": 40}

    def test_init(self):
        self.assertEqual("KFC", self.kfc.name)
        self.assertEqual(100, self.kfc.capacity)
        self.assertEqual([], self.kfc.waiters)

    def test_wrong_name_with_spaces(self):
        with self.assertRaises(Exception) as ex:
            self.kfc.name = "   "

        self.assertEqual("Invalid name!", str(ex.exception))

    def test_wrong_name_without_spaces(self):
        with self.assertRaises(Exception) as ex:
            self.kfc.name = ""

        self.assertEqual("Invalid name!", str(ex.exception))

    def test_wrong_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.kfc.capacity = -1

        self.assertEqual("Invalid capacity!", str(ex.exception))

    def test_add_waiter_without_capacity(self):
        self.kfc.capacity = 0
        self.assertEqual("No more places!", self.kfc.add_waiter("Bob"))

    def test_add_waiter_with_already_existing_one(self):
        waiter_name = "Adam"
        self.kfc.waiters.append({'name': waiter_name})
        self.assertEqual(f"The waiter {waiter_name} already exists!", self.kfc.add_waiter(waiter_name))

    def test_add_waiter_with_correct_input(self):
        waiter_name = "Adam"
        new_waiter = {"name": waiter_name}
        self.assertEqual(f"The waiter {waiter_name} has been added.", self.kfc.add_waiter(waiter_name))
        self.assertEqual([new_waiter], self.kfc.waiters)

    def test_remove_waiter_with_correct_input(self):
        waiter_name = "Adam"
        new_waiter = {"name": waiter_name}
        self.kfc.waiters.append(new_waiter)
        self.assertEqual(f"The waiter {waiter_name} has been removed.", self.kfc.remove_waiter(waiter_name))
        self.assertEqual([], self.kfc.waiters)

    def test_remove_waiters_with_incorect_input(self):
        waiter_name = "Adam"
        new_waiter = {"name": waiter_name}
        searched_name = "Bob"
        self.kfc.waiters.append(new_waiter)
        self.assertEqual(f"No waiter found with the name {searched_name}.", self.kfc.remove_waiter(searched_name))
        self.assertEqual([new_waiter], self.kfc.waiters)

    def test_get_waiter_with_none(self):
        self.kfc.waiters.append(self.first_waiter)
        self.kfc.waiters.append(self.second_waiter)
        result = self.kfc.waiters
        self.assertEqual(result, self.kfc.get_waiters())

    def test_get_waiters_with_salary_equal_to_the_minimal(self):
        self.kfc.waiters.append(self.first_waiter)
        self.kfc.waiters.append(self.second_waiter)
        result = self.kfc.waiters
        self.assertEqual(result, self.kfc.get_waiters(30, 100))

    def test_get_waiters_with_salary_less_than_the_minimal(self):
        self.kfc.waiters.append(self.first_waiter)
        self.kfc.waiters.append(self.second_waiter)
        self.assertEqual([self.second_waiter], self.kfc.get_waiters(35, 100))

    def test_get_waiters_with_salary_higher_than_the_maximum(self):
        self.kfc.waiters.append(self.first_waiter)
        self.kfc.waiters.append(self.second_waiter)
        self.assertEqual([self.first_waiter], self.kfc.get_waiters(10, 35))

    def test_get_waiters_with_salary_equal_to_the_maximum(self):
        self.kfc.waiters.append(self.first_waiter)
        self.kfc.waiters.append(self.second_waiter)
        result = self.kfc.waiters
        self.assertEqual(result, self.kfc.get_waiters(10, 40))

    def test_of_get_total_earnings(self):
        self.kfc.waiters.append(self.first_waiter)
        self.kfc.waiters.append(self.second_waiter)
        result = 70
        self.assertEqual(result, self.kfc.get_total_earnings())




if __name__ == "__main__":
    main()
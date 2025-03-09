from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.marvel = ToyStore()

    def test_init(self):
        result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(result, self.marvel.toy_shelf)

    def test_add_toy_wrong_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.marvel.add_toy("P", "Blaster")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_with_same_toy_already_in(self):
        self.marvel.toy_shelf["D"] = "Blaster"
        with self.assertRaises(Exception) as ex:
            self.marvel.add_toy("D", "Blaster")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_with_toy_already_in(self):
        self.marvel.toy_shelf["D"] = "Blaster"
        with self.assertRaises(Exception) as ex:
            self.marvel.add_toy("D", "Lego")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_with_correct_input(self):
        toy_name = "Blaster"
        self.assertEqual(f"Toy:{toy_name} placed successfully!", self.marvel.add_toy("B", toy_name))
        self.assertEqual(toy_name, self.marvel.toy_shelf["B"])

    def test_remove_toy_with_wrong_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.marvel.remove_toy("Z", "Yo-Yo")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_with_wrong_toy_name(self):
        self.marvel.toy_shelf["A"] = "Yo-Yo"
        with self.assertRaises(Exception) as ex:
            self.marvel.remove_toy("A", "Blaster")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_with_correct_input(self):
        self.marvel.toy_shelf["A"] = "Yo-Yo"
        toy_name = "Yo-Yo"
        self.assertEqual(f"Remove toy:{toy_name} successfully!", self.marvel.remove_toy("A", toy_name))
        self.assertEqual(None, self.marvel.toy_shelf["A"])






if __name__ == "__main__":
    main()
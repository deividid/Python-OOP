from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Lion", "Cat", "ARRR")

    def test_of_init(self):

        self.assertEqual("Lion", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("ARRR", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_of_sound_method(self):

        self.assertEqual("Lion makes ARRR", self.mammal.make_sound())

    def test_of_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_of_info(self):
        self.assertEqual("Lion is of type Cat", self.mammal.info())



if __name__ == "__main__":
    main()
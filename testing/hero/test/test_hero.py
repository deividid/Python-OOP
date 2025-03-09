from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Pesho", 10, 100, 20)

    def test_init(self):
        self.assertEqual("Pesho", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_battle_with_yourself(self):
        enemy = Hero("Pesho", 10, 100, 20)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_no_blood(self):
        self.hero.health = 0
        opponent = Hero("Gosho", 9, 99, 19)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(opponent)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_opponent_with_no_health(self):
        opponent = Hero("Gosho", 9, -12, 19)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(opponent)

        self.assertEqual("You cannot fight Gosho. He needs to rest", str(ex.exception))

    def test_battle_with_weaker_opponent(self):
        new_opponent = Hero("Gosho", 9, 99, 10)
        result = self.hero.battle(new_opponent)
        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(25, self.hero.damage)

    def test_battle_with_a_draw(self):
        self.opponent = Hero("Tosho", 10, 80, 30)
        result = self.hero.battle(self.opponent)
        self.assertEqual("Draw", result)
        self.assertEqual(-200, self.hero.health)
        self.assertEqual(-120, self.opponent.health)

    def test_battle_with_a_loss(self):
        self.god_of_war = Hero("Kratos", 100, 300, 500)
        result = self.hero.battle(self.god_of_war)
        self.assertEqual("You lose", result)
        self.assertEqual(101, self.god_of_war.level)
        self.assertEqual(105, self.god_of_war.health)
        self.assertEqual(505, self.god_of_war.damage)

    def test_of_str_method(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_result, self.hero.__str__())










if __name__ == "__main__":
    main()
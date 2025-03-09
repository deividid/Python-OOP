from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Nadal", 30, 100)
        self.other_player = TennisPlayer("Federer", 32, 85)
        self.other_player.wins.append("Wimbledon")

    def test_init(self):
        self.assertEqual("Nadal", self.player.name)
        self.assertEqual(30, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_wrong_name_with_less_than_two_characters(self):

        with self.assertRaises(Exception) as ex:
            self.player.name = "I"

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_wrong_name_with_two_characters(self):

        with self.assertRaises(Exception) as ex:
            self.player.name = "It"

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_wrong_age(self):

        with self.assertRaises(Exception) as ex:
            self.player.age = 16

        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_add_new_win(self):
        self.player.add_new_win("Wimbledon")
        self.assertEqual(["Wimbledon"], self.player.wins)

    def test_add_new_win_with_existing_win(self):
        tournament_name = "Wimbledon"
        self.assertEqual(f"{tournament_name} has been already added to the list of wins!", self.other_player.add_new_win(tournament_name))

    def test_lt_method_with_more_points_for_the_first_player(self):
        result = f'{self.player.name} is a better player than {self.other_player.name}'
        self.assertEqual(result, self.player < self.other_player)

    def test_lt_method_with_more_point_for_the_second_player(self):
        self.other_player.points = 200
        result = f'{self.other_player.name} is a top seeded player and he/she is better than {self.player.name}'
        self.assertEqual(result, self.player < self.other_player)

    def test_lt_method_with_equal_points(self):
        self.other_player.points = 100
        result = f'{self.player.name} is a better player than {self.other_player.name}'
        self.assertEqual(result, self.player < self.other_player)

    def test_of_str_method_with_less_than_two_wins(self):
        result = f"Tennis Player: {self.player.name}\n" \
               f"Age: {self.player.age}\n" \
               f"Points: {self.player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(result, self.player.__str__())

    def test_of_str_method_with_more_than_one_win(self):
        self.player.wins.append("First")
        self.player.wins.append("Second")
        result = f"Tennis Player: {self.player.name}\n" \
               f"Age: {self.player.age}\n" \
               f"Points: {self.player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(result, self.player.__str__())


if __name__ == "__main__":
    main()

from encapsulation.football_team_generator.project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []

    def add_player(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"

        else:
            return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        player = [footballer for footballer in self.__players if footballer.name == player_name]
        if player:
            self.__players.remove(player[0])
            return player[0]

        else:
            return f"Player {player_name} not found"

p = Player("Pall", 1, 3, 5, 7)

print("Player name:", p.name)

print("Points sprint:", p._Player__sprint)
print("Points dribble:", p._Player__dribble)
print("Points passing:", p._Player__passing)
print("Points shooting:", p._Player__shooting)
print("\ncalling the __str__ method")
print(p)
print("\nAbout the team")
t = Team("Best", 10)
print("Team name:", t._Team__name)
print("Teams points:", t._Team__rating)
print("Teams players:", len(t._Team__players))
print(t.add_player(p))
print(t.add_player(p))
print("Teams players:", len(t._Team__players))
print(t.remove_player("Pall"))
print(t.remove_player("Pall"))

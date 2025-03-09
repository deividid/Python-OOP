from typing import List

from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, p: Player):
        if p.guild != "Unaffiliated":
            if p.guild == self.name:
                return f"Player {p.name} is already in the guild."
            else:
                return f"Player {p.name} is in another guild."

        else:
            self.players.append(p)
            p.guild = self.name
            return f"Welcome player {p.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if player_name not in [p.name for p in self.players]:
            return f"Player {player_name} is not in the guild."

        else:
            for p in self.players:
                if p.name == player_name:
                    self.players.remove(p)
                    p.guild = "Unaffiliated"
                    return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}"
        for p in self.players:
            result += f"\n{p.player_info()}"

        return result



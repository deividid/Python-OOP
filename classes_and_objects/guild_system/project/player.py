class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill, mana_cost):
        if skill in self.skills.keys():
            return "Skill already added"

        else:
            self.skills[skill] = mana_cost
            return f"Skill {skill} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}"

        for s, m in self.skills.items():
            result += f"\n==={s} - {m}"

        return result



from project.peaks.base_peak import BasePeak

class SummitPeak(BasePeak):
    RECOMMENDED_GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def __init__(self, name, elevation):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return self.RECOMMENDED_GEAR

    def calculate_difficulty_level(self):
        if 1500 <= self.elevation <= 2500:
            return "Advanced"

        elif self.elevation > 2500:
            return "Extreme"

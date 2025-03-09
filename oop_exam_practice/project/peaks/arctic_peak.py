from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    RECOMMENDED_GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def __init__(self, name, elevation):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return self.RECOMMENDED_GEAR

    def calculate_difficulty_level(self):
        if 2000 <= self.elevation <= 3000:
            return "Advanced"

        elif self.elevation > 3000:
            return "Extreme"

from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    types_of_climbers = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    types_of_peaks = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def register_climber(self, climber_type, climber_name):
        if climber_type not in self.types_of_climbers.keys():
            return f"{climber_type} doesn't exist in our register."

        if climber_name in [c.name for c in self.climbers]:
            return f"{climber_name} has been already registered."

        new_climber = self.types_of_climbers[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type, peak_name, peak_elevation):

        if peak_type not in self.types_of_peaks.keys():
            return f"{peak_type} is an unknown type of peak."

        new_peak = self.types_of_peaks[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name, peak_name, gear: List):
        for climber in self.climbers:
            if climber.name == climber_name:
                for peak in self.peaks:
                    if peak.name == peak_name:
                        missing_gear = []
                        for g in peak.get_recommended_gear():
                            if g not in gear:
                                missing_gear.append(g)

                        if len(missing_gear) > 0:
                            climber.is_prepared = False
                            return f"{climber_name} is not prepared to climb {peak_name}. " \
                                   f"Missing gear: {', '.join(sorted(missing_gear))}."
                        else:
                            return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name, peak_name):
        if climber_name not in [c.name for c in self.climbers]:
            return f"Climber {climber_name} is not registered yet."

        if peak_name not in [p.name for p in self.peaks]:
            return f"Peak {peak_name} is not part of the wish list."

        for c in self.climbers:
            if c.name == climber_name:
                for p in self.peaks:
                    if p.name == peak_name:

                        if c.is_prepared and c.can_climb():
                            c.climb(p)
                            return f"{climber_name} conquered {peak_name} " \
                                   f"whose difficulty level is {p.difficulty_level}."
                        elif not c.is_prepared:
                            return f"{climber_name} will need to be better prepared next time."

                        elif c.can_climb() != True:
                            c.rest()
                            return f"{climber_name} needs more strength to climb {peak_name} " \
                                   f"and is therefore taking some rest."

    def get_statistics(self):
        successfull_climbers = [c for c in self.climbers if len(c.conquered_peaks) > 0]
        unique_peaks = []
        for c in successfull_climbers:
            for i in range(len(c.conquered_peaks)):
                if c.conquered_peaks[i] not in unique_peaks:
                    unique_peaks.append(c.conquered_peaks[i])

        result = f"Total climbed peaks: {len(unique_peaks)}" \
                 f"\n**Climber's statistics:**"
        for c in sorted(successfull_climbers, key=lambda c: (-len(c.conquered_peaks), c.name)):
            if len(c.conquered_peaks) > 1:
                c.conquered_peaks.sort()

            result += f"\n{c.__str__()}"

        return result


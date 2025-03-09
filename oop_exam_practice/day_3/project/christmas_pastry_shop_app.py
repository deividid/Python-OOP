from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    types_of_delicacies = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    types_of_booths = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.types_of_delicacies.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.types_of_delicacies[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.types_of_booths.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.types_of_booths[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for b in self.booths:
            if not b.is_reserved and b.capacity >= number_of_people:
                b.reserve(number_of_people)
                return f"Booth {b.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if booth_number not in [b.booth_number for b in self.booths]:
            raise Exception(f"Could not find booth {booth_number}!")

        if delicacy_name not in [d.name for d in self.delicacies]:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        for b in self.booths:
            if b.booth_number == booth_number:
                for d in self.delicacies:
                    if d.name == delicacy_name:

                        b.delicacy_orders.append(d)
                        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        for b in self.booths:
            if b.booth_number == booth_number:
                bill = b.price_for_reservation + sum([d.price for d in b.delicacy_orders])
                self.income += bill
                b.delicacy_orders.clear()
                b.price_for_reservation = 0
                b.is_reserved = False
                return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

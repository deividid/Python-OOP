from project.customer import Customer

from project.dvd import DVD
from typing import List


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []
    @staticmethod
    def dvd_capacity(self):
        return 15
    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, disk: DVD):
        if len(self.dvds) < self.dvd_capacity(self):
            self.dvds.append(disk)

    def rent_dvd(self, customer_id, dvd_id):
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            else:
                return "DVD is already rented"

        else:
            if dvd.age_restriction > customer.age:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

            else:
                dvd.is_rented = True
                customer.rented_dvds.append(dvd)
                return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for people in self.customers:
            result += f"{str(people)}\n"

        for disk in self.dvds:
            result += f"{str(disk)}\n"

        return result












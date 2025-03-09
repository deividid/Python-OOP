from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    types_of_robots = {"FemaleRobot": FemaleRobot, "MaleRobot": MaleRobot}
    types_of_services = {"MainService": MainService, "SecondaryService": SecondaryService}

    def add_service(self, service_type, service_name):
        if service_type not in self.types_of_services.keys():
            raise Exception("Invalid service type!")

        new_service = self.types_of_services[service_type](service_name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.types_of_robots.keys():
            raise Exception("Invalid robot type!")

        new_robot = self.types_of_robots[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        for r in self.robots:
            if r.name == robot_name:
                for s in self.services:
                    if s.name == service_name:
                        if (r.__class__.__name__ == "MaleRobot" and s.__class__.__name__ == "SecondaryService") or (r.__class__.__name__ == "FemaleRobot" and s.__class__.__name__ == "MainService"):
                            return "Unsuitable service."

                        elif len(s.robots) >= s.capacity:
                            raise Exception("Not enough capacity for this robot!")

                        else:
                            s.robots.append(r)
                            self.robots.remove(r)
                            return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name, service_name):
        for s in self.services:
            if s.name == service_name:
                if robot_name not in [r.name for r in s.robots]:
                    raise Exception("No such robot in this service!")

                for r in s.robots:
                    if r.name == robot_name:
                        self.robots.append(r)
                        s.robots.remove(r)
                        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name):
        count = 0
        for s in self.services:
            if s.name == service_name:
                count = len(s.robots)
                for r in s.robots:
                    r.eating()

        return f"Robots fed: {count}."

    def service_price(self, service_name):
        total_price = sum(r.price for s in self.services if s.name == service_name for r in s.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ""
        for s in self.services:
            result += f"{s.details()}\n"

        return result[:-1]

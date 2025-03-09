from project.services.base_service import BaseService


class MainService(BaseService):
    MAIN_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.MAIN_CAPACITY)

    def details(self):
        if len(self.robots) > 0:
            return f"{self.name} Main Service:\nRobots: {' '.join([r.name for r in self.robots])}"

        else:
            return f"{self.name} Main Service:\nRobots: none"

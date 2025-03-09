from project.services.base_service import BaseService


class SecondaryService(BaseService):
    SECONDARY_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.SECONDARY_CAPACITY)

    def details(self):
        if len(self.robots) > 0:
            return f"{self.name} Secondary Service:\nRobots: {' '.join([r.name for r in self.robots])}"

        else:
            return f"{self.name} Secondary Service:\nRobots: none"

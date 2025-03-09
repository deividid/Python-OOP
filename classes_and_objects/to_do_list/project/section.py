from typing import List

from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, t: Task):
        if t in self.tasks:
            return f"Task is already in the section {self.name}"

        else:
            self.tasks.append(t)
            return f"Task {t.details()} is added to the section"

    def complete_task(self, task_name):
        if task_name not in [t.name for t in self.tasks]:
            return f"Could not find task with the name {task_name}"

        else:
            for t in self.tasks:
                if t.name == task_name:
                    t.completed = True
                    return f"Completed task {task_name}"

    def clean_section(self):
        count = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                count += 1

        return f"Cleared {count} tasks."

    def view_section(self):
        result = f"Section {self.name}:"

        for t in self.tasks:
            result += f"\n{t.details()}"

        return result



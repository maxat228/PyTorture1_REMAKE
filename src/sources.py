import os
from random import randint
from typing import Iterator
from src.task import Task


class FileSource:
    def get_tasks(self) -> Iterator[Task]:
        tasks = []
        path = os.path.join(os.path.dirname(__file__), "..", "tasks.txt")
        with open(path, encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue
                task_id, payload = line.strip().split(",", 1)
                tasks.append(Task(task_id=int(task_id), payload=payload))
        return iter(tasks)


class RandomSource:
    def __init__(self, count: int = 1) -> None:
        self.count = count

    def get_tasks(self) -> Iterator[Task]:
        tasks = []
        for number in range(self.count):
            task_id = randint(1, 100)
            payload = f"Случайная задача #{number}"
            tasks.append(Task(task_id=task_id, payload=payload))
        return iter(tasks)


class ApiSource:
    def get_tasks(self) -> Iterator[Task]:
        tasks = [
            Task(task_id=101, payload="Пример 1"),
            Task(task_id=102, payload="Пример 2"),
            Task(task_id=103, payload="Пример 3"),
        ]
        return iter(tasks)
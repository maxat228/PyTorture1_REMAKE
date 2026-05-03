from typing import List
from src.protocols import TaskSource
from src.task import Task


def load_tasks(source: TaskSource, task_list: List[Task]) -> None:
    for task in source.get_tasks():
        task_list.append(task)
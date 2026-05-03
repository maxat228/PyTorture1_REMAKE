from typing import Iterator
from src.task import Task
from src.protocols import TaskSource
from src.loader import load_tasks
from src.sources import FileSource, RandomSource, ApiSource

# Создаем источники
file_source = FileSource()
random_source = RandomSource(3)
api = ApiSource()

# Проверяем контракт
for source in [file_source, random_source, api]:
    if isinstance(source, TaskSource):
        print(f"{source.__class__.__name__} соответствует контракту TaskSource")
    else:
        print(f"{source.__class__.__name__} не соответствует контракту TaskSource")

print("-" * 50)

# Загружаем задачи
tasks = []
for source in [file_source, random_source, api]:
    load_tasks(source, tasks)
print(f"Количество задач: {len(tasks)}")

print("-" * 50)

# Выводим задачи
for number, task in enumerate(tasks):
    print(f"{number + 1}: {task.id}, {task.payload}")

print("-" * 50)

# Показываем расширяемость
new_tasks = []

class NewSource:
    def __init__(self, count: int = 1) -> None:
        self.count = count

    def get_tasks(self) -> Iterator[Task]:
        tasks = []
        for i in range(self.count):
            payload = input(f"Введите описание задачи #{i + 1}: ")
            tasks.append(Task(task_id=1000 + i, payload=payload))
        return iter(tasks)

new_source = NewSource(2)
load_tasks(new_source, new_tasks)

for number, task in enumerate(new_tasks):
    print(f"Новая задача {number + 1}: {task.id}, {task.payload}")

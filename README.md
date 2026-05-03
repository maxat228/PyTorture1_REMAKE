# Лабораторная работа №1. Источники задач и контракты (РЕМЕЙК)

---

## Описание
Реализация подсистемы приёма задач с использованием Duck Typing и Protocol.
Задачи поступают из различных источников, не связанных наследованием, но соблюдающих единый контракт.

---

## Структура проекта

```
PyTorture1_REMAKE/
├── src/
│ ├── __init__.py
│ ├── task.py # Класс Task (id, payload)
│ ├── protocols.py # Protocol TaskSource с @runtime_checkable
│ ├── sources.py # FileSource, RandomSource, ApiSource
│ └── loader.py # Функция load_tasks
├── tests/
│ ├── __init__.py
│ └── test_sources.py # Тесты
├── tasks.txt # Файл с задачами для FileSource
├── .gitignore
└── README.md
```

---

## Реализация
- **Protocol TaskSource** — контракт с методом `get_tasks() -> Iterator[Task]`
- **@runtime_checkable** — поддержка `isinstance` для проверки контракта
- **FileSource** — читает задачи из `tasks.txt`
- **RandomSource** — генерирует случайные задачи
- **ApiSource** — имитация ответа от API
- **load_tasks** — загрузка задач из любого источника в список
- Нет общего базового класса — только протокол

---

## Запуск тестов
```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

Покрытие тестами составляет 98%

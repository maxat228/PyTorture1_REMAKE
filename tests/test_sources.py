from src.protocols import TaskSource
from src.task import Task
from src.loader import load_tasks
from src.sources import FileSource, RandomSource, ApiSource


def test_file_source_is_tasksource():
    file_source = FileSource()
    assert isinstance(file_source, TaskSource) is True


def test_random_source_is_tasksource():
    random_source = RandomSource(3)
    assert isinstance(random_source, TaskSource) is True


def test_api_source_is_tasksource():
    api_source = ApiSource()
    assert isinstance(api_source, TaskSource) is True


def test_not_task_source():
    source = []
    assert isinstance(source, TaskSource) is False


def test_get_tasks_returns_iterator():
    for source in [FileSource(), RandomSource(3), ApiSource()]:
        iterator = source.get_tasks()
        assert hasattr(iterator, '__iter__')
        assert hasattr(iterator, '__next__')


def test_get_tasks_elements_are_tasks():
    file_source = FileSource()
    random_source = RandomSource(3)
    api_source = ApiSource()
    assert all(isinstance(task, Task) for task in file_source.get_tasks())
    assert all(isinstance(task, Task) for task in random_source.get_tasks())
    assert all(isinstance(task, Task) for task in api_source.get_tasks())


def test_load_tasks_adds_to_list():
    tasks = []
    load_tasks(ApiSource(), tasks)
    assert len(tasks) != 0 and len(tasks) == 3
    assert all(isinstance(task, Task) for task in tasks)


def test_load_tasks_works_with_all_sources():
    tasks = []
    for source in [FileSource(), RandomSource(3), ApiSource()]:
        load_tasks(source, tasks)
    assert len(tasks) == 11


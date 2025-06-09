import pytest
from use_cases.task_use_case import TaskUseCase
from domain.task import Task

class FakeTaskRepository:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def add(self, task):
        task.id = self.counter
        self.counter += 1
        self.tasks.append(task)
        return task

    def get_all(self):
        return self.tasks

def test_create_task():
    repo = FakeTaskRepository()
    use_case = TaskUseCase(repo)

    task = use_case.create_task("Fazer exercício", "Descrição do exercício")

    assert isinstance(task, Task)
    assert task.title == "Fazer exercício"
    assert task.description == "Descrição do exercício"
    assert not task.is_done
    assert task.id == 1

def test_list_tasks():
    repo = FakeTaskRepository()
    use_case = TaskUseCase(repo)

    use_case.create_task("Tarefa 1", "Descrição 1")
    use_case.create_task("Tarefa 2", "Descrição 2")

    tasks = use_case.list_tasks()

    assert len(tasks) == 2
    assert tasks[0].title == "Tarefa 1"
    assert tasks[1].title == "Tarefa 2"

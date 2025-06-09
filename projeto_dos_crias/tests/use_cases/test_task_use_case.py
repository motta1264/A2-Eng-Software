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

    def find_by_group_id(self, group_id):
        return [t for t in self.tasks if t.grupo_id == group_id]

def test_create_task():
    repo = FakeTaskRepository()
    use_case = TaskUseCase(repo)

    task = use_case.create("Fazer exercício", grupo_id=1)

    assert isinstance(task, Task)
    assert task.titulo == "Fazer exercício"
    assert task.grupo_id == 1

def test_tasks_by_group():
    repo = FakeTaskRepository()
    use_case = TaskUseCase(repo)

    use_case.create("Tarefa 1", grupo_id=1)
    use_case.create("Tarefa 2", grupo_id=2)
    use_case.create("Tarefa 3", grupo_id=1)

    group_1_tasks = use_case.get_by_group(1)
    assert len(group_1_tasks) == 2
    assert all(t.grupo_id == 1 for t in group_1_tasks)

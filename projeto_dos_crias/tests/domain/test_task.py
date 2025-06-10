from domain.task import Task


def test_task_creation():
    task = Task(
        id=1, title="Exercício 1", description="Resolver questão 1", is_done=False
    )
    assert task.id == 1
    assert task.title == "Exercício 1"
    assert task.description == "Resolver questão 1"
    assert task.is_done is False

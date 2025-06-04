# use_cases/task_use_case.py

class TaskUseCase:
    def __init__(self, repository):
        self.repository = repository

    def create_task(self, title, description):
        from domain.task import Task
        task = Task(id=None, title=title, description=description)
        return self.repository.add(task)

    def list_tasks(self):
        return self.repository.get_all()

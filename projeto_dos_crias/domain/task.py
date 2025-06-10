# domain/task.py


class Task:
    def __init__(self, id, title, description, is_done=False):
        self.id = id
        self.title = title
        self.description = description
        self.is_done = is_done

    def mark_as_done(self):
        self.is_done = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_done": self.is_done,
        }

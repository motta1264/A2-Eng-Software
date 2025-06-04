class User:
    def __init__(self, id, name, email, password_hashed, faculdade=None, cursos=None):
        self.id = id
        self.name = name
        self.email = email
        self.password_hashed = password_hashed
        self.faculdade = faculdade
        self.cursos = cursos or ""

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "faculdade": self.faculdade,
            "cursos": self.cursos
        }

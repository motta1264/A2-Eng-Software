import pytest
from use_cases.user_use_case import UserUseCase
from domain.user import User

class FakeUserRepository:
    def __init__(self):
        self.users = []

    def save(self, user):
        return self.add(user)

    def add(self, user):
        self.users.append(user)
        return user

    def find_by_email(self, email):
        for u in self.users:
            if u.email == email:
                return u
        return None

def test_register_user():
    repo = FakeUserRepository()
    use_case = UserUseCase(repo)

    user = use_case.register("Alice", "alice@email.com", "senha")

    assert isinstance(user, User)
    assert user.name == "Alice"
    assert user.email == "alice@email.com"

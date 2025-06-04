# use_cases/user_use_case.py

import hashlib
from domain.user import User

class UserUseCase:
    def __init__(self, repository):
        self.repository = repository

    def hash_password(self, plain):
        return hashlib.sha256(plain.encode()).hexdigest()

    def register(self, name, email, plain_password):
        hashed = self.hash_password(plain_password)
        user = User(id=None, name=name, email=email, password_hashed=hashed)
        return self.repository.add(user)

    def login(self, email, plain_password):
        user = self.repository.find_by_email(email)
        if not user:
            return None
        hashed_input = self.hash_password(plain_password)
        if hashed_input == user.password_hashed:
            return user
        return None

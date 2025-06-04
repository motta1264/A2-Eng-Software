# infra/repositories/user_repository_sqlite.py

import sqlite3
from domain.user import User

class UserRepository:
    def __init__(self, connection):
        self.conn = connection
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()

        # Criação da tabela se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password_hashed TEXT NOT NULL
            )
        """)

        # Verifica se as colunas novas existem, se não, adiciona
        cursor.execute("PRAGMA table_info(users);")
        columns = [col[1] for col in cursor.fetchall()]

        if "faculdade" not in columns:
            cursor.execute("ALTER TABLE users ADD COLUMN faculdade TEXT;")

        if "cursos" not in columns:
            cursor.execute("ALTER TABLE users ADD COLUMN cursos TEXT;")

        self.conn.commit()


    def add(self, user):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, email, password_hashed)
            VALUES (?, ?, ?)
        """, (user.name, user.email, user.password_hashed))
        self.conn.commit()
        user.id = cursor.lastrowid
        return user

    def find_by_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, name, email, password_hashed, faculdade, cursos FROM users WHERE email = ?
        """, (email,))
        row = cursor.fetchone()
        return User(*row) if row else None
    
    def update_user(self, user):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE users SET name = ?, email = ?, faculdade = ?, cursos = ? WHERE id = ?
        """, (user.name, user.email, user.faculdade, user.cursos, user.id))
        self.conn.commit()

    def find_by_id(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, name, email, password_hashed, faculdade, cursos FROM users WHERE id = ?
        """, (user_id,))
        row = cursor.fetchone()
        return User(*row) if row else None

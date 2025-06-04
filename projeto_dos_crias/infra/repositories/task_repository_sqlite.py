# infra/repositories/task_repository_sqlite.py

import sqlite3
from domain.task import Task

class TaskRepository:
    def __init__(self, connection):
        self.conn = connection
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                is_done BOOLEAN DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add(self, task):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO tasks (title, description, is_done) VALUES (?, ?, ?)', 
                       (task.title, task.description, task.is_done))
        self.conn.commit()
        task.id = cursor.lastrowid
        return task

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, title, description, is_done FROM tasks')
        rows = cursor.fetchall()
        return [Task(*row) for row in rows]

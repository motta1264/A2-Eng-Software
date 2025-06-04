# app/main.py

from flask import Flask
from app.routes.task_routes import create_task_routes
from infra.repositories.task_repository_sqlite import TaskRepository
from infra.db.database import get_connection
from use_cases.task_use_case import TaskUseCase

def create_app():
    app = Flask(__name__)

    conn = get_connection()
    task_repo = TaskRepository(conn)
    task_use_case = TaskUseCase(task_repo)

    task_routes = create_task_routes(task_use_case)
    app.register_blueprint(task_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

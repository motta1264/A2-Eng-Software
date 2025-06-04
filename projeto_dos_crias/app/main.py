from flask import Flask, render_template, session
from app.routes.task_routes import create_task_routes
from app.routes.user_routes import create_user_routes
from infra.repositories.task_repository_sqlite import TaskRepository
from infra.repositories.user_repository_sqlite import UserRepository
from infra.db.database import get_connection
from use_cases.task_use_case import TaskUseCase
from use_cases.user_use_case import UserUseCase
from app.routes.group_routes import create_group_routes
from infra.repositories.group_repository_sqlite import GroupRepository
from use_cases.group_use_case import GroupUseCase

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.secret_key = "segredo123"  # Necessário para sessão

    conn = get_connection()
    task_repo = TaskRepository(conn)
    user_repo = UserRepository(conn)

    task_use_case = TaskUseCase(task_repo)
    user_use_case = UserUseCase(user_repo)

    app.register_blueprint(create_task_routes(task_use_case))
    app.register_blueprint(create_user_routes(user_use_case))

    group_repo = GroupRepository(conn)
    group_use_case = GroupUseCase(group_repo)
    app.register_blueprint(create_group_routes(group_use_case))
    
    @app.route("/")
    def home():
        return render_template("index.html")


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

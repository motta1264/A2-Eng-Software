# app/routes/task_routes.py

from flask import Blueprint, request, jsonify

def create_task_routes(task_use_case):
    task_bp = Blueprint('task', __name__)

    @task_bp.route("/tasks", methods=["GET"])
    def get_tasks():
        tasks = task_use_case.list_tasks()
        return jsonify([task.to_dict() for task in tasks])

    @task_bp.route("/tasks", methods=["POST"])
    def create_task():
        data = request.json
        task = task_use_case.create_task(data["title"], data.get("description", ""))
        return jsonify(task.to_dict()), 201

    return task_bp

from flask import Blueprint, request, jsonify
from app.models.task import Task
from app.services.task_service import TaskService

task_routes = Blueprint('task_routes', __name__)
task_service = TaskService()

@task_routes.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = task_service.add_task(data['title'], data.get('description', ''))
    return jsonify(task), 201

@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = task_service.get_all_tasks()
    return jsonify(tasks), 200

@task_routes.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_service.get_task(task_id)
    if task:
        return jsonify(task), 200
    return jsonify({'error': 'Task not found'}), 404

@task_routes.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    updated_task = task_service.update_task(task_id, data.get('title'), data.get('description'), data.get('completed'))
    if updated_task:
        return jsonify(updated_task), 200
    return jsonify({'error': 'Task not found'}), 404

@task_routes.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    success = task_service.delete_task(task_id)
    if success:
        return jsonify({'message': 'Task deleted'}), 204
    return jsonify({'error': 'Task not found'}), 404
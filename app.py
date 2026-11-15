
from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary storage for tasks
tasks = {}
next_task_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Task Management REST API",
        "status": "running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(list(tasks.values())), 200


@app.route("/tasks", methods=["POST"])
def add_task():
    global next_task_id

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Task title is required"}), 400

    task = {
        "id": next_task_id,
        "title": title.strip(),
        "description": data.get("description", ""),
        "completed": False
    }

    tasks[next_task_id] = task
    next_task_id += 1

    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = tasks.get(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    del tasks[task_id]

    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

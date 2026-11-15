
import pytest
from app import app, tasks


@pytest.fixture
def client():
    app.config["TESTING"] = True

    tasks.clear()

    global next_task_id
    import app as application
    application.next_task_id = 1

    with app.test_client() as client:
        yield client

    tasks.clear()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []


def test_add_task(client):
    response = client.post(
        "/tasks",
        json={"title": "Learn DevOps"}
    )
    assert response.status_code == 201
    assert response.get_json()["title"] == "Learn DevOps"


def test_get_individual_task(client):
    client.post("/tasks", json={"title": "Test Task"})

    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.get_json()["title"] == "Test Task"


def test_delete_task(client):
    client.post("/tasks", json={"title": "Delete Me"})

    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Task deleted successfully"


def test_invalid_task(client):
    response = client.post("/tasks", json={})

    assert response.status_code == 400

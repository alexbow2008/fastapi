from fastapi.testclient import TestClient

from behind_a_proxy.tutorial001 import app

client = TestClient(app, root_path="/api/v1")

openapi_schema = {
    "openapi": "3.0.2",
    "info": {"title": "FastAPI", "version": "0.1.0"},
    "paths": {
        "/api/v1/app": {
            "get": {
                "summary": "Read Main",
                "operationId": "read_main_app_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {"application/json": {"schema": {}}},
                    }
                },
            }
        }
    },
}


def test_openapi():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json() == openapi_schema


def test_main():
    response = client.get("/app")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World", "root_path": "/api/v1"}

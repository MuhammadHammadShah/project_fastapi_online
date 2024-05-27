from fastapi.testclient import TestClient
from fastapi_helloworld_online.main import app


def test_root_path():
    client = TestClient(app=app) # We have to put a parameter name "app" and assign an object(of FastAPI ) which is imported
    respone = client.get("/")
    assert respone.status_code == 200
    assert respone.json() == {"Hello": "World"}

def test_piaic_description():
    client = TestClient(app=app)
    respone = client.get("/piaic/")
    assert respone.status_code == 200
    assert respone.json() == {"organization" : "piaic"}



def test_third_forfailure():
    client = TestClient(app=app)
    respone = client.get("/piaic/")
    assert respone.status_code == 200
    assert respone.json() == {"organizations" : "World"}
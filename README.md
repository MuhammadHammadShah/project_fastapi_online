# Hello World with Fastapi

**I you have to download some packages in poetry use this syntax this will add the package with latest version to _pyproject.toml_ `poetry add (any package name)` _replace `any package name` with the desire package_**

**`http://127.0.0.1:8000/docs` opens a swagger UI called `Mock sserver` useful for testing the routes of pages like here we have `home` `piaic`**


1. `poetry new fastapi_helloworld_online`
2. `cd fastapi_helloworld_online`
3. Select your project with VSCode 
4. open file `pyproject.toml`
5. `poetry add fastapi "uvicorn[standard]"` 
6. `poetry shell` *is used to activate the environment*
7. `poetry run uvicorn fastapi_helloworld_online.main:app --reload ` *To start server.*



```
If the intelisess for  fastapi is not showing up in vscode restart the vscode.
```
**The reason behind it is environment is not selected. Restart Vscode and the environment will be selected.**

**`Fastapi` is a framework used for coding and `uvicorn` make the system a server-like so we can use fastapi.**

```[tool.poetry]
name = "fastapi-helloworld-online"
version = "0.1.0"
description = ""
authors = ["Muhammad_Hammad_Shah <Hammad4455shah5544@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.111.0"
uvicorn = {extras = ["standard"], version = "^0.29.0"}


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

create a new file name `main.py` location `fastapi_helloworld_online\main.py`


**In folder tree we have `poetry.lock`. This lock the versions of packages with respect to the day the project was create. If the the project is cloned 10 months ago the project will have packages with version of 10 months ago.**


**In this code `poetry run uvicorn fastapi_helloworld_online.main:app --reload ` `--reload` reload the page by itself and `uvicorn` make the system server.**


# Writing Tests
<p>In Test code file the test process test all the functions in file we want to test, also tell the details for it, either there are 1000 functions</p>

1. Whenvere we create project before we submit the project we have to create `test code` to find out any bug before deployment.
2. We will be using `pytest` for `test_code` 
3. The test file should name `test...` just for ease.
4. To add pytest to project `poetry add pytest`
5. To run pytest and test the Functions `poetry run pytest -v`

**Test code is at `tests/test_main.py`**
```
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
```

from fastapi import FastAPI

# FastAPI is the object(class) it will manage everything 
# @ is a decorator

app = FastAPI()

@app.get("/") # root folder
def index():
    return {"Hello":"World"}


@app.get("/piaic/") 
def index():
    return {"organization":"piaic"}



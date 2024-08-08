from fastapi import FastAPI

app = FastAPI()


@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


# poetry run uvicorn index:app 
# "fastapi-dev": "pip3 install -r requirements.txt && python3 -m uvicorn api.index:app --reload",

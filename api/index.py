from fastapi import FastAPI

app = FastAPI()


# app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")


@app.get("/api/python")
def hello_world():
    return {"message": "Hello from GenAI SaaS Boilerplate."}


# poetry run uvicorn index:app
# "fastapi-dev": "pip3 install -r requirements.txt && python3 -m uvicorn api.index:app --reload",


# Run the server: poetry run uvicorn crypto_trading_bot.main:app --reload --host 0.0.0.0 --port 8000
# Open the following urls:
# 	- http://localhost:8000
# 	- http://localhost:8000/docs
# 	- http://localhost:8000/openapi.json

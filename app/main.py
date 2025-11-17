from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello from GKE with GitOps"}

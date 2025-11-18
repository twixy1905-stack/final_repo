from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello from GKE with GitOps"}

@app.get("/live")
def liveness():
    # Simple "am I alive" check
    return {"status": "ok"}

@app.get("/ready")
def readiness():
    # Here you could later check DB, external services, etc.
    return {"status": "ready"}

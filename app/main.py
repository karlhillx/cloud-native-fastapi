from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Cloud-Native FastAPI Example", version="0.1.0")

class HealthResponse(BaseModel):
    status: str
    service: str

@app.get("/health", response_model=HealthResponse)
def health_check():
    return {"status": "ok", "service": "cloud-native-fastapi"}

@app.get("/")
def root():
    return {"message": "Hello from a modern, cloud-native FastAPI service 🚀"}

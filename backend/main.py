from fastapi import FastAPI

app = FastAPI(
    title="Attendance Management System",
    description="Backend API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Attendance Management System 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "Server is running successfully!"
    }
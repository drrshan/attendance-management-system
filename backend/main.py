from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router

app = FastAPI(
    title="Attendance Management System",
    description="Backend API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


app.include_router(auth_router)
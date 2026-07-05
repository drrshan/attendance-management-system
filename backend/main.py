from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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


class LoginRequest(BaseModel):
    email: str
    password: str


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


@app.post("/login")
def login(login: LoginRequest):
    return {
        "message": "Login request received successfully!",
        "email": login.email
    }
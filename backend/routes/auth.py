from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(login: LoginRequest):

    users = [
        {
            "email": "admin@college.com",
            "password": "admin123",
            "role": "admin"
        },
        {
            "email": "faculty@college.com",
            "password": "faculty123",
            "role": "faculty"
        },
        {
            "email": "student@college.com",
            "password": "student123",
            "role": "student"
        }
    ]

    for user in users:
        if (
            login.email == user["email"]
            and login.password == user["password"]
        ):
            return {
                "success": True,
                "message": "Login Successful",
                "user": {
                    "email": user["email"],
                    "role": user["role"]
                },
                "token": "demo-jwt-token"
            }

    return {
        "success": False,
        "message": "Invalid email or password"
    }
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.database import get_db
from models.user import User
from utils.security import verify_password

router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(login: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.email == login.email
    ).first()

    if not user:
        return {
            "success": False,
            "message": "Invalid email or password"
        }

    if not verify_password(login.password, user.password):
        return {
            "success": False,
            "message": "Invalid email or password"
        }

    return {
        "success": True,
        "message": "Login Successful",
        "user": {
            "email": user.email,
            "role": user.role
        },
        "token": "demo-jwt-token"
    }
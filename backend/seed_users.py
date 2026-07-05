from database.database import SessionLocal
from models.user import User
from utils.security import hash_password
db = SessionLocal()

existing_user = db.query(User).filter(
    User.email == "admin@college.com"
).first()

if existing_user:
    print("Admin user already exists!")

else:
    admin = User(
        name="Administrator",
        email="admin@college.com",
        password=hash_password("admin123"),
        role="admin"
    )

    db.add(admin)
    db.commit()

    print("✅ Admin user created successfully!")

db.close()
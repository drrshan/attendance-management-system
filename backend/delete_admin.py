from database.database import SessionLocal
from models.user import User

db = SessionLocal()

user = db.query(User).filter(
    User.email == "admin@college.com"
).first()

if user:
    db.delete(user)
    db.commit()
    print("✅ Admin deleted successfully!")
else:
    print("❌ Admin user not found.")

db.close()
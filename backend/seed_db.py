from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models

def seed():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Ensure S001 and S002 exist for the dashboard demo
    if db.query(models.Student).filter(models.Student.student_id == "S001").first():
        print("S001 already exists.")
    else:
        print("Adding S001 and S002...")
        demo_students = [
            models.Student(
                student_id="S001",
                name="Aarav Sharma",
                attendance_rate=0.88,
                gpa=3.5,
                financial_aid=False,
                failed_courses=0,
                extracurricular_activities=True,
                risk_category="Safe",
                dropout_risk_score=0.15
            ),
            models.Student(
                student_id="S002",
                name="Priya Patel",
                attendance_rate=0.52,
                gpa=2.1,
                financial_aid=True,
                failed_courses=2,
                extracurricular_activities=False,
                risk_category="Critical",
                dropout_risk_score=0.88
            )
        ]
        db.add_all(demo_students)
        db.commit()

    db.close()
    print("Done seeding backend.")

if __name__ == "__main__":
    seed()

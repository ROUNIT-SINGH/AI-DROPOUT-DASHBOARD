from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models
import random

def seed():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Check if we already have the 50 students seeded
    if db.query(models.Student).count() >= 50:
        print("Database already seeded with 50 students.")
        
        # Optionally, we can clear and reseed if you want it to be exact
        # For now we'll just clear it so we can re-seed cleanly
        db.query(models.Student).delete()
        db.commit()
    else:
        # Clear existing demo students if any
        db.query(models.Student).delete()
        db.commit()

    print("Adding 50 students from data...")
    demo_students = [
        models.Student(
            student_id="S001",
            name="Ananya Mehta",
            attendance_rate=0.72,
            gpa=3.02,
            financial_aid=False,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.21
        ),
        models.Student(
            student_id="S002",
            name="Arjun Agarwal",
            attendance_rate=0.81,
            gpa=2.96,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.22
        ),
        models.Student(
            student_id="S003",
            name="Aadhya Yadav",
            attendance_rate=0.72,
            gpa=2.97,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.21
        ),
        models.Student(
            student_id="S004",
            name="Vivaan Agarwal",
            attendance_rate=0.91,
            gpa=3.36,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.14
        ),
        models.Student(
            student_id="S005",
            name="Navya Patel",
            attendance_rate=0.80,
            gpa=3.42,
            financial_aid=False,
            failed_courses=2,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.22
        ),
        models.Student(
            student_id="S006",
            name="Vihaan Agarwal",
            attendance_rate=0.65,
            gpa=2.55,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.33
        ),
        models.Student(
            student_id="S007",
            name="Sara Mishra",
            attendance_rate=0.51,
            gpa=2.24,
            financial_aid=False,
            failed_courses=2,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.45
        ),
        models.Student(
            student_id="S008",
            name="Anika Gupta",
            attendance_rate=0.94,
            gpa=3.48,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.08
        ),
        models.Student(
            student_id="S009",
            name="Aadhya Verma",
            attendance_rate=0.71,
            gpa=2.72,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.28
        ),
        models.Student(
            student_id="S010",
            name="Anika Verma",
            attendance_rate=0.88,
            gpa=3.83,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.11
        ),
        models.Student(
            student_id="S011",
            name="Shaurya Singh",
            attendance_rate=0.72,
            gpa=3.35,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.22
        ),
        models.Student(
            student_id="S012",
            name="Aditya Mehta",
            attendance_rate=0.57,
            gpa=2.61,
            financial_aid=False,
            failed_courses=3,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.43
        ),
        models.Student(
            student_id="S013",
            name="Riya Sharma",
            attendance_rate=0.73,
            gpa=3.12,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.20
        ),
        models.Student(
            student_id="S014",
            name="Aadhya Gupta",
            attendance_rate=0.54,
            gpa=2.65,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=False,
            risk_category="At Risk",
            dropout_risk_score=0.36
        ),
        models.Student(
            student_id="S015",
            name="Diya Yadav",
            attendance_rate=0.72,
            gpa=2.66,
            financial_aid=False,
            failed_courses=2,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.33
        ),
        models.Student(
            student_id="S016",
            name="Anika Yadav",
            attendance_rate=1.00,
            gpa=3.87,
            financial_aid=False,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.01
        ),
        models.Student(
            student_id="S017",
            name="Ayaan Verma",
            attendance_rate=0.76,
            gpa=3.15,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.18
        ),
        models.Student(
            student_id="S018",
            name="Diya Singh",
            attendance_rate=0.92,
            gpa=3.64,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.07
        ),
        models.Student(
            student_id="S019",
            name="Anika Yadav",
            attendance_rate=0.55,
            gpa=2.54,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.37
        ),
        models.Student(
            student_id="S020",
            name="Aarav Yadav",
            attendance_rate=0.64,
            gpa=2.87,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.30
        ),
        models.Student(
            student_id="S021",
            name="Vihaan Yadav",
            attendance_rate=0.56,
            gpa=1.95,
            financial_aid=False,
            failed_courses=3,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.50
        ),
        models.Student(
            student_id="S022",
            name="Saanvi Yadav",
            attendance_rate=0.89,
            gpa=3.72,
            financial_aid=False,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.07
        ),
        models.Student(
            student_id="S023",
            name="Vivaan Yadav",
            attendance_rate=0.64,
            gpa=2.32,
            financial_aid=False,
            failed_courses=0,
            extracurricular_activities=False,
            risk_category="At Risk",
            dropout_risk_score=0.31
        ),
        models.Student(
            student_id="S024",
            name="Aadhya Mehta",
            attendance_rate=0.78,
            gpa=3.52,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.18
        ),
        models.Student(
            student_id="S025",
            name="Ananya Yadav",
            attendance_rate=0.76,
            gpa=3.54,
            financial_aid=False,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.14
        ),
        models.Student(
            student_id="S026",
            name="Navya Mehta",
            attendance_rate=0.73,
            gpa=3.18,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.19
        ),
        models.Student(
            student_id="S027",
            name="Arjun Mehta",
            attendance_rate=0.53,
            gpa=2.41,
            financial_aid=True,
            failed_courses=2,
            extracurricular_activities=False,
            risk_category="At Risk",
            dropout_risk_score=0.43
        ),
        models.Student(
            student_id="S028",
            name="Saanvi Verma",
            attendance_rate=0.67,
            gpa=2.56,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.32
        ),
        models.Student(
            student_id="S029",
            name="Vihaan Singh",
            attendance_rate=0.86,
            gpa=3.62,
            financial_aid=False,
            failed_courses=0,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.09
        ),
        models.Student(
            student_id="S030",
            name="Riya Mishra",
            attendance_rate=0.52,
            gpa=1.69,
            financial_aid=True,
            failed_courses=2,
            extracurricular_activities=False,
            risk_category="At Risk",
            dropout_risk_score=0.50
        ),
        models.Student(
            student_id="S031",
            name="Aarav Yadav",
            attendance_rate=0.54,
            gpa=1.66,
            financial_aid=False,
            failed_courses=3,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.54
        ),
        models.Student(
            student_id="S032",
            name="Krishna Mehta",
            attendance_rate=0.99,
            gpa=3.97,
            financial_aid=False,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.01
        ),
        models.Student(
            student_id="S033",
            name="Saanvi Jain",
            attendance_rate=0.68,
            gpa=2.37,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.29
        ),
        models.Student(
            student_id="S034",
            name="Aarav Patel",
            attendance_rate=0.64,
            gpa=2.55,
            financial_aid=False,
            failed_courses=0,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.29
        ),
        models.Student(
            student_id="S035",
            name="Diya Mishra",
            attendance_rate=0.81,
            gpa=2.98,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.18
        ),
        models.Student(
            student_id="S036",
            name="Myra Yadav",
            attendance_rate=0.58,
            gpa=2.55,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.35
        ),
        models.Student(
            student_id="S037",
            name="Ishaan Agarwal",
            attendance_rate=0.88,
            gpa=3.68,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.12
        ),
        models.Student(
            student_id="S038",
            name="Vihaan Gupta",
            attendance_rate=0.89,
            gpa=3.59,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.13
        ),
        models.Student(
            student_id="S039",
            name="Sara Mehta",
            attendance_rate=0.80,
            gpa=3.63,
            financial_aid=True,
            failed_courses=2,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.20
        ),
        models.Student(
            student_id="S040",
            name="Sara Jain",
            attendance_rate=0.91,
            gpa=3.54,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=False,
            risk_category="Safe",
            dropout_risk_score=0.12
        ),
        models.Student(
            student_id="S041",
            name="Diya Patel",
            attendance_rate=0.82,
            gpa=3.68,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.10
        ),
        models.Student(
            student_id="S042",
            name="Kiara Yadav",
            attendance_rate=0.86,
            gpa=3.16,
            financial_aid=True,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.14
        ),
        models.Student(
            student_id="S043",
            name="Navya Jain",
            attendance_rate=0.58,
            gpa=2.41,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.37
        ),
        models.Student(
            student_id="S044",
            name="Shaurya Patel",
            attendance_rate=0.63,
            gpa=2.25,
            financial_aid=False,
            failed_courses=0,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.32
        ),
        models.Student(
            student_id="S045",
            name="Arjun Sharma",
            attendance_rate=0.76,
            gpa=3.05,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.23
        ),
        models.Student(
            student_id="S046",
            name="Aditya Jain",
            attendance_rate=0.84,
            gpa=3.40,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.16
        ),
        models.Student(
            student_id="S047",
            name="Aarav Mehta",
            attendance_rate=0.68,
            gpa=3.00,
            financial_aid=True,
            failed_courses=1,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.27
        ),
        models.Student(
            student_id="S048",
            name="Ishaan Jain",
            attendance_rate=0.71,
            gpa=2.44,
            financial_aid=False,
            failed_courses=1,
            extracurricular_activities=False,
            risk_category="At Risk",
            dropout_risk_score=0.31
        ),
        models.Student(
            student_id="S049",
            name="Ananya Patel",
            attendance_rate=0.79,
            gpa=3.07,
            financial_aid=True,
            failed_courses=2,
            extracurricular_activities=True,
            risk_category="Safe",
            dropout_risk_score=0.26
        ),
        models.Student(
            student_id="S050",
            name="Anika Verma",
            attendance_rate=0.70,
            gpa=2.36,
            financial_aid=False,
            failed_courses=2,
            extracurricular_activities=True,
            risk_category="At Risk",
            dropout_risk_score=0.36
        ),
    ]
    db.add_all(demo_students)
    db.commit()

    db.close()
    print("Done seeding backend with 50 students.")

if __name__ == "__main__":
    seed()

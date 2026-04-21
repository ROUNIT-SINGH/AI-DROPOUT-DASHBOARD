from sqlalchemy import Column, Integer, String, Float, Boolean, Text, PickleType
try:
    from pgvector.sqlalchemy import Vector
    HAS_PGVECTOR = True
except ImportError:
    HAS_PGVECTOR = False
from .database import Base, DATABASE_URL

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    
    # Features for ML
    attendance_rate = Column(Float)
    gpa = Column(Float)
    financial_aid = Column(Boolean)
    failed_courses = Column(Integer)
    extracurricular_activities = Column(Boolean)
    
    # Prediction
    dropout_risk_score = Column(Float, nullable=True)
    risk_category = Column(String, nullable=True)

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, index=True)
    message = Column(Text)
    is_user = Column(Boolean)
    # Use Vector if PostgreSQL, otherwise fallback to PickleType for local testing
    if DATABASE_URL.startswith("postgresql") and HAS_PGVECTOR:
        embedding = Column(Vector(384), nullable=True)
    else:
        embedding = Column(PickleType, nullable=True)

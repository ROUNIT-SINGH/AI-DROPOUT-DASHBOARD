from pydantic import BaseModel
from typing import Optional, List

class StudentBase(BaseModel):
    student_id: str
    name: str
    attendance_rate: float
    gpa: float
    financial_aid: bool
    failed_courses: int
    extracurricular_activities: bool

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    dropout_risk_score: Optional[float]
    risk_category: Optional[str]

    class Config:
        from_attributes = True

class ChatRequest(BaseModel):
    student_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str

class BatchPredictItem(BaseModel):
    student_id: str
    attendance: float
    current_marks: float
    previous_marks: float
    fee_status: str

class BatchPredictRequest(BaseModel):
    students: List[BatchPredictItem]

class BatchPredictResponseItem(BaseModel):
    student_id: str
    risk: str
    riskScore: float

class BatchPredictResponse(BaseModel):
    predictions: List[BatchPredictResponseItem]

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
from .ml import predict
from .chatbot import agent

models.Base.metadata.create_all(bind=database.engine)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Dropout Dashboard API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Dropout Dashboard API"}

@app.post("/students/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    db_student = models.Student(**student.model_dump())
    
    # Calculate risk score automatically upon creation
    features = {
        "attendance_rate": db_student.attendance_rate,
        "gpa": db_student.gpa,
        "financial_aid": db_student.financial_aid,
        "failed_courses": db_student.failed_courses,
        "extracurricular_activities": db_student.extracurricular_activities
    }
    
    risk_score = predict.get_dropout_risk(features)
    db_student.dropout_risk_score = risk_score
    db_student.risk_category = "High" if risk_score > 0.7 else ("Medium" if risk_score > 0.4 else "Low")
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: str, db: Session = Depends(database.get_db)):
    student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/chat", response_model=schemas.ChatResponse)
def chat_with_student(chat_req: schemas.ChatRequest, db: Session = Depends(database.get_db)):
    student = db.query(models.Student).filter(models.Student.student_id == chat_req.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found for context")
        
    context = f"Student {student.name} has a GPA of {student.gpa}, attendance of {student.attendance_rate*100}%. Risk category: {student.risk_category}."
    reply = agent.get_chat_response(chat_req.message, context)
    
    # Save to history
    user_msg = models.ChatHistory(student_id=student.student_id, message=chat_req.message, is_user=True)
    bot_msg = models.ChatHistory(student_id=student.student_id, message=reply, is_user=False)
    db.add(user_msg)
    db.add(bot_msg)
    db.commit()
    
    return {"reply": reply}

@app.post("/predict_batch", response_model=schemas.BatchPredictResponse)
def predict_batch(req: schemas.BatchPredictRequest):
    predictions = []
    for s in req.students:
        # Map frontend features to ML features
        features = {
            "attendance_rate": s.attendance / 100.0,
            "gpa": s.current_marks / 25.0, # Approximate scale 0-100 to 0-4.0
            "financial_aid": s.fee_status == "Pending",
            "failed_courses": 1 if s.current_marks < 40 else 0,
            "extracurricular_activities": False
        }
        
        risk_score = predict.get_dropout_risk(features)
        
        # Determine risk category based on frontend logic / model scale
        if risk_score > 0.7:
            risk = "Critical"
            score = 90.0
        elif risk_score > 0.4:
            risk = "At Risk"
            score = 60.0
        else:
            risk = "Safe"
            score = 20.0
            
        predictions.append(schemas.BatchPredictResponseItem(
            student_id=s.student_id,
            risk=risk,
            riskScore=score
        ))
        
    return schemas.BatchPredictResponse(predictions=predictions)

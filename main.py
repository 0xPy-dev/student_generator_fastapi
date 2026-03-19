from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
import pandas as pd
from model import load_model

messages = {
    "dropout": "⚠️ Есть высокий риск того, что студент может отчислиться.\nРекомендуется уделить больше внимания учебе и вовлеченности.",
    "enrolled": "📚 Студент продолжает обучение.\nРезультаты стабильные, но есть потенциал для улучшения.",    
    "graduate": "🎓 Отличные показатели!\nВысокая вероятность успешного окончания обучения."
}

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
def root():
    return FileResponse("frontend/index.html")

model, encoder = load_model()

class Student(BaseModel):
    Marital_status: int
    Application_mode: int
    Application_order: int
    Course: int
    Daytime_evening_attendance: int
    Previous_qualification: int
    Admission_grade: float = Field(..., ge=0, le=100)
    Gender: int
    Age_at_enrollment: int = Field(..., ge=0, le=100)
    Scholarship_holder: int


# ====== PREDICT ======
@app.post("/predict")
def predict(student: Student):

    df = pd.DataFrame([student.dict()])

    pred = model.predict(df)[0]
    result = encoder.inverse_transform([pred])[0]
    result = messages[result.lower()]
    
    return {"prediction": result}
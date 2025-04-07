from fastapi import FastAPI
from pydantic import BaseModel
from database.db import get_patient_history, get_doctors_by_specialty
from models.nlp_model import detect_intent, extract_symptoms
from utils.matcher import get_specialty_from_symptoms
from fastapi.middleware.cors import CORSMiddleware
# Initialize FastAPI app
app = FastAPI()

origins = [
    "http://localhost:3000",  # for React (Vite/Cra) dev
    "http://127.0.0.1:8000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # allow all headers
)
# Request model
class Query(BaseModel):
    patient_id: str
    message: str

# POST endpoint for virtual assistant
@app.post("/assistant/")
def process_query(query: Query):
    # Step 1: Get patient history
    patient_data = get_patient_history(query.patient_id)
    if not patient_data:
        return {"error": "Patient not found"}

    # Step 2: Use NLP model to detect intent and extract symptoms
    intent = detect_intent(query.message)
    symptoms = extract_symptoms(query.message)

    # Step 3: Determine required specialty
    if intent == "follow-up":
        specialty = patient_data[-2] if len(patient_data) >= 2 else "General Physician"  # last_diagnosis assumed at -2
    else:
        specialty = get_specialty_from_symptoms(symptoms)

    # Step 4: Get available doctors from DB
    doctors = get_doctors_by_specialty(specialty)
    if not doctors:
        return {
            "intent": intent,
            "symptoms": symptoms,
            "assigned_doctor": None,
            "message": f"No doctor available for {specialty} currently."
        }

    # Step 5: Return response with doctor assignment
    try:
        doctor = doctors[0]  # Get first available doctor
        return {
            "intent": intent,
            "symptoms": symptoms,
            "assigned_doctor": {
                "name": doctor[1] if len(doctor) > 1 else "Unknown",
                "specialty": doctor[2] if len(doctor) > 2 else specialty,
                "slot": doctor[3] if len(doctor) > 3 else "TBD"
            },
            "message": "Appointment scheduled!"
        }
    except Exception as e:
        return {"error": f"Unexpected error occurred: {str(e)}"}

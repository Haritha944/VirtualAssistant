def get_specialty_from_symptoms(symptoms):
    mapping = {
        "fever": "General Physician",
        "cough": "Pulmonologist",
        "sore throat": "ENT",
        "headache": "Neurologist",
        "chest pain": "Cardiologist"
    }
    for symptom in symptoms:
        if symptom in mapping:
            return mapping[symptom]
    return "General Physician"

import sqlite3

# Connect to SQLite DB
def connect_db():
    return sqlite3.connect("data/doctors.db")  # make sure this path is correct

# Fetch patient history by patient_id
def get_patient_history(patient_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    result = cursor.fetchone()
    conn.close()
    return result

# Fetch doctors by specialty
def get_doctors_by_specialty(specialty):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors WHERE specialty = ?", (specialty,))
    results = cursor.fetchall()
    conn.close()
    return results

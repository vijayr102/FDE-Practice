import pandas as pd
from dotenv import load_dotenv
import os
import psycopg

load_dotenv()


def load_data():
    file_path = os.getenv("DATA_FILE")
    pd_df = pd.read_csv(file_path)
    with psycopg.connect(os.getenv("CONN")) as conn:
        with conn.cursor() as cur:
            for index, row in pd_df.iterrows():
                risk_score = 0
                risk_score += 3 if row['number_inpatient'] >= 3 else 0
                risk_score += 2 if row['number_emergency'] >= 2 else 0
                risk_score += 1 if row['number_outpatient'] >= 3 else 0
                risk_score +=1 if row['time_in_hospital'] >= 7 else 0
                risk_score += 1 if row['num_medications'] >= 20 else 0
                risk_level = 'HIGH' if risk_score >= 5 else 'MEDIUM' if risk_score >= 3 else 'LOW'
                cur.execute(
                    "INSERT INTO encounters(encounter_id, patient_nbr, age, time_in_hospital,number_inpatient, number_emergency, number_outpatient,num_medications, num_lab_procedures,discharge_disposition_id, admission_type_id,readmitted, risk_score, risk_level"+
                    ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        row['encounter_id'], row['patient_nbr'], row['age'], row['time_in_hospital'],
                        row['number_inpatient'], row['number_emergency'], row['number_outpatient'],
                        row['num_medications'], row['num_lab_procedures'], row['discharge_disposition_id'],
                        row['admission_type_id'], row['readmitted'], risk_score, risk_level
                    )
                )
                cur.execute(
                                "INSERT INTO interventions ("
                                "encounter_id, status, assigned_to, notes, created_at, updated_at"
                                ") VALUES (%s, %s, %s, %s, %s, %s)",
                                (
                                    row['encounter_id'], 'PENDING', None, None, pd.Timestamp.now(), pd.Timestamp.now()
                                )
                            )
            conn.commit()

load_data()
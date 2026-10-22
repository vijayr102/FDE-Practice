from database import get_connection


def get_encounters():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM encounters")
            encounters = cur.fetchall()
            return encounters

def get_encounter_by_id(encounter_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM encounters WHERE encounter_id = %s", (encounter_id,))
            encounter = cur.fetchone()
            return encounter

def get_care_queue():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT interventions.* FROM encounters join interventions on encounters.encounter_id = interventions.encounter_id where risk_level in ('HIGH','MEDIUM') order by risk_score desc")
            care_queue = cur.fetchall()
            return care_queue

def get_intervention_by_id(intervention_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM interventions WHERE intervention_id = %s", (intervention_id,))
            intervention = cur.fetchone()
            return intervention

def update_intervention_assignee(intervention_id, assigned_to):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE interventions SET assigned_to = %s, updated_at = NOW(), status = 'IN_PROGRESS' WHERE intervention_id = %s RETURNING *", (assigned_to, intervention_id))
            updated_intervention = cur.fetchone()
            conn.commit()
            return updated_intervention

def get_operational_summary():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    COUNT(*) AS total_encounters,
                    SUM(CASE WHEN risk_level = 'HIGH' THEN 1 ELSE 0 END) AS high_risk_count,
                    SUM(CASE WHEN risk_level = 'MEDIUM' THEN 1 ELSE 0 END) AS medium_risk_count,
                    SUM(CASE WHEN risk_level = 'LOW' THEN 1 ELSE 0 END) AS low_risk_count
                FROM encounters
            """)
            summary = cur.fetchone()
            cur.execute("""
                    select sum(case when status = 'COMPLETED' then 1 else 0 end) as completed_interventions,
                       sum(case when status = 'PENDING' then 1 else 0 end) as pending_interventions,
                       sum(case when status = 'IN_PROGRESS' then 1 else 0 end) as assigned_interventions
                       from interventions 
            """)
            status_counts = cur.fetchone()
            print("Operational Summary:", summary)
            print("Status Counts:", status_counts)
            return summary, status_counts

"""{
  "number": "112345",
  "age": "20-30",
  "timeinhospital": "10",
  "inpatientvisits": "10",
  "emergencyvisits": "5",
  "medications": "5"
}"""
def create_encounter(encounter: dict):
    with get_connection() as conn:
        with conn.cursor() as cur:
            risk_score = 0
            risk_score += 3 if int(encounter['inpatientvisits']) >= 3 else 0
            risk_score += 2 if int(encounter['emergencyvisits']) >= 2 else 0
            #risk_score += 1 if int(encounter['outpatientvisits']) >= 3 else 0
            risk_score +=1 if int(encounter['timeinhospital']) >= 7 else 0
            risk_score += 1 if int(encounter['medications']) >= 20 else 0
            risk_level = 'HIGH' if risk_score >= 5 else 'MEDIUM' if risk_score >= 3 else 'LOW'
            cur.execute("""
                INSERT INTO encounters (encounter_id, patient_nbr, age, time_in_hospital, number_inpatient, number_emergency, num_medications, risk_score, risk_level,discharge_disposition_id,admission_type_id,readmitted)
                VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *
            """, (encounter['number'], encounter['age'], encounter['timeinhospital'], encounter['inpatientvisits'], encounter['emergencyvisits'], encounter['medications'], risk_score, risk_level, 0,0,0))
            new_encounter = cur.fetchone()
            conn.commit()
            return new_encounter

def get_readmission_risk_analysis():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    select 
                    SUM(CASE WHEN risk_level = 'HIGH' THEN 1 ELSE 0 END) as high_risk_patients,
                    SUM(CASE WHEN risk_level = 'HIGH' AND readmitted= '<30' THEN 1 ELSE 0 END) as high_risk_readmissions
                    from encounters
                """)
                risk_analysis = cur.fetchall()
                high_risk_readmissions = f"{(risk_analysis[0]['high_risk_readmissions'] / risk_analysis[0]['high_risk_patients'])*100:.2f}" if risk_analysis[0]['high_risk_patients'] > 0 else "0%"
                return {**risk_analysis[0], "high_risk_readmissions_rate": high_risk_readmissions}
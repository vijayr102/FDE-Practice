from datetime import datetime
from typing import Optional

from pydantic import BaseModel

#(2278392, 8222157, '[0-10)', 1, 0, 0, 0, 1, 41, 25, 6, 'NO', Decimal('0.0000'), 'LOW')

class Encounter(BaseModel):
    encounter_id: int
    patient_nbr: int
    age: str
    time_in_hospital: int
    number_inpatient: int
    number_emergency: int
    number_outpatient: int
    num_medications: int
    num_lab_procedures: int
    discharge_disposition_id: int
    admission_type_id: int
    readmitted: str
    risk_score: float
    risk_level: str

class Intervention(BaseModel):
    intervention_id: int
    encounter_id: int
    assigned_to: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    notes: Optional[str] = None
    status: str
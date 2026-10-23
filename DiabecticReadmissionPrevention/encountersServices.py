from repository import create_encounter, get_encounter_by_id, get_encounters, get_intervention_by_id
from fastapi import APIRouter
from models import Encounter, Intervention

router = APIRouter()

@router.get("/encounters",response_model=list[Encounter])
def get_encounters_endpoint():
    encounters = get_encounters()
    return encounters

@router.get("/encounters/{encounter_id}", response_model=Encounter)
def get_encounter_by_id_endpoint(encounter_id: int):
    encounter = get_encounter_by_id(encounter_id)
    if encounter:
        return encounter
    else:
        return {"error": "Encounter not found"}, 404

@router.post("/createencounters", response_model=Encounter)
def create_encounter_endpoint(encounter_data: dict):
    return create_encounter(encounter_data)


@router.get("/searchPatient", response_model=list[Encounter])
def search_patient_endpoint(patient_number: str = None, risk_score: float = None, risk_level: str = None):
    encounters = get_encounters(patient_number=patient_number, risk_score=risk_score, risk_level=risk_level)
    return encounters

@router.get("/patients/{patient_id}", response_model=Intervention)
def get_patient_interventions(patient_id: str):
    encounters = get_encounters(patient_number=patient_id)
    print(encounters)
    interventions = get_intervention_by_id(encounter_id=encounters[0]['encounter_id'])
    return interventions
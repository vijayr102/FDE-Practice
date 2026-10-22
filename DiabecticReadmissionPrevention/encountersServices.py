from repository import create_encounter, get_encounter_by_id, get_encounters
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
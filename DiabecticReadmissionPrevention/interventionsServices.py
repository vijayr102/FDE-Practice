from models import Intervention
from repository import get_care_queue, get_intervention_by_id, update_intervention_assignee
from fastapi import APIRouter

router = APIRouter()

@router.get("/care-queue",response_model=list[Intervention])
def get_care_queue_endpoint():
    care_queue = get_care_queue()
    return care_queue

@router.get("/interventions/{intervention_id}", response_model=Intervention)
def get_intervention_by_id_endpoint(intervention_id: str):
    intervention = get_intervention_by_id(intervention_id=intervention_id)
    if intervention:
        return intervention
    else:
        return {"error": "Intervention not found"}, 404

@router.patch("/update-interventions/{intervention_id}", response_model=Intervention)
def update_intervention(intervention_id: int, assigned_to: str):
    # Here you would typically update the intervention in the database
    # For demonstration purposes, we'll just return the updated intervention
    intervention = update_intervention_assignee(intervention_id, assigned_to)
    return intervention


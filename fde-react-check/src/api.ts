import type { Encounter, Intervention, SearchCriteria } from './types';

export const API_BASE = 'http://127.0.0.1:3003';

export function hasCriteria({ patientNumber, riskLevel, riskScore }: SearchCriteria): boolean {
  return Boolean(patientNumber || riskLevel || riskScore !== undefined);
}

export async function searchPatients(criteria: SearchCriteria, signal?: AbortSignal): Promise<Encounter[]> {
  const params = new URLSearchParams();
  if (criteria.patientNumber) params.append('patient_number', criteria.patientNumber);
  if (criteria.riskLevel) params.append('risk_level', criteria.riskLevel);
  if (criteria.riskScore !== undefined) params.append('risk_score', criteria.riskScore.toString());

  const response = await fetch(`${API_BASE}/searchPatient?${params}`, { signal });
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
}

export async function fetchEncounters(offset: number = 0, limit: number = 10, signal?: AbortSignal): Promise<Encounter[]> {
    const response = await fetch(`${API_BASE}/encounters?limit=${limit}&offset=${offset}`, { signal });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data: Encounter[] = await response.json();
    return data;
}

export async function fetchPatientDetails(patientId: number, signal?: AbortSignal): Promise<Intervention> {
            const response = await fetch(`${API_BASE}/patients/${patientId}`, { signal });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const patient: Intervention = await response.json();
            return patient;

        }

export async function updatedInterventions(interventionId: number, assignedTo: string, signal?: AbortSignal): Promise<Intervention> {
    const response = await fetch(`${API_BASE}/update-interventions/${interventionId}?assigned_to=${assignedTo}`, {
        method: 'PATCH',
        signal
    });
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const updatedIntervention: Intervention = await response.json();
    return updatedIntervention;
}

        // window.addEventListener("DOMContentLoaded", fetchPatientDetails);

        // document.querySelector('form').addEventListener('submit', async (event) => {
        //     event.preventDefault();
        //     const interventionData = {
        //         intervention_id: document.getElementById('interventionId').value,
        //         encounter_id: document.getElementById('encounterId').value,
        //         status: document.getElementById('status').value,
        //         assigned_to: document.getElementById('assignedTo').value,
        //         notes: document.getElementById('notes').value,
        //         created_at: document.getElementById('createdAt').value
        //     };
        //     try {
        //         const response = await fetch(`http://127.0.0.1:3003/update-interventions/${interventionData.intervention_id}?assigned_to=${interventionData.assigned_to}`, {
        //             method: 'PATCH'
        //         });
        //         console.log('Update response status:', response.status);
        //         let data = await response.json();
        //        document.getElementById("updated-interventions").innerHTML = `
        //             <tr>
        //                 <td>${data.intervention_id}</td>
        //                 <td>${data.encounter_id}</td>
        //                 <td>${data.status}</td>
        //                 <td>${data.assigned_to}</td>
        //                 <td>${data.notes}</td>
        //                 <td>${data.created_at}</td>
        //             </tr>
        //         `;
        //         console.log(data);
        //     } catch (error) {
        //         console.error('There was a problem with the fetch operation:', error);
        //     }

        // });
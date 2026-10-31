import {interventionRow} from '../components/interventionRow';
import {type Intervention} from '../types';
import { useEffect, useState,type SubmitEvent } from 'react';
import { fetchPatientDetails, updatedInterventions } from '../api';
import { useParams } from 'react-router-dom';

export function PatientDetails() {
    const [intervention, setIntervention] = useState<Intervention | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [assignedTo, setAssignedTo] = useState('');
    const patientId = useParams();

    useEffect(() => {
        if (!patientId) return;
        const controller = new AbortController();
        fetchPatientDetails(parseInt(patientId.patientId as string), controller.signal)
            .then((data) => {
                setIntervention(data);
                setError(null);
            })
            .catch((err) => {
                if (controller.signal.aborted) return; // a newer request replaced this one
                console.error('Error fetching patient details:', err);
                setError(String(err));
                setIntervention(null);
            });

        }, [patientId]);
        const handleSubmit = async (e: SubmitEvent<HTMLFormElement>) => {
            e.preventDefault();
            if (!intervention) return;
            try {
                const updated = await updatedInterventions(intervention.intervention_id, assignedTo);
                setIntervention(updated);
                setError(null);
            } catch (err) {
                setError(String(err));
            }

        };

    return (
        <section className="patient-details">
        <h1>Patient Details</h1>
        {error && <p role="alert">{error}</p>}
        {!error && !intervention && <p>Loading...</p>}
        {intervention && (
            <section>
            <section className="patient-details-section">
                <h2>Details of Patient</h2>
                <div id="patient-details">
                    <section className="Patient Intervention">
                        <form className="search-form" onSubmit={handleSubmit}>
                            <div className="field">
                        <label htmlFor="interventionId">Intervention ID:</label>
                        <input type="text" id="interventionId" name="interventionId" value={intervention?.intervention_id} readOnly/>
                    </div>
                    <div className="field">
                        <label htmlFor="encounterId">Encounter ID:</label>
                        <input type="text" id="encounterId" name="encounterId" value={intervention?.encounter_id} readOnly/>
                    </div>
                    <div className="field">
                        <label htmlFor="status">Status:</label>
                        <input type="text" id="status" name="status" value={intervention?.status} readOnly/>
                    </div>
                    <div className="field">
                        <label htmlFor="assignedTo">Assigned To:</label>
                        <input value={assignedTo} onChange={(e) => setAssignedTo(e.target.value)} type="text" id="assignedTo" name="assignedTo" />
                    </div>
                    <div className="field">
                        <label htmlFor="notes">Notes:</label>
                        <textarea id="notes" name="notes" value={intervention?.notes} readOnly></textarea>
                    </div>
                    <div className="field">
                        <label htmlFor="createdAt">Created At:</label>
                        <input type="text" id="createdAt" name="createdAt" value={intervention?.created_at} readOnly/>
                    </div>
                    <button className="btn btn-primary" type="submit">Update Intervention</button>
                </form>
            </section>
        </div>
    </section>
        <section className="updated-interventions">
            <table className="patient-table">
                <thead>
                    <tr>
                        <th>Intervention ID</th>
                        <th>Encounter ID</th>
                        <th>Status</th>
                        <th>Assigned To</th>
                        <th>Notes</th>
                        <th>Created At</th>
                    </tr>
                </thead>
                <tbody id="updated-interventions">
                    {interventionRow( intervention )}
                </tbody>
                </table>
        </section>
    </section>
    )}
    </section>
    );
}
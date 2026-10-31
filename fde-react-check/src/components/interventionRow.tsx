import {type Intervention} from '../types';

export function interventionRow(intervention: Intervention) {
    return (
        <tr>
            <td>{intervention.intervention_id}</td>
            <td>{intervention.encounter_id}</td>
            <td>{intervention.status}</td>
            <td>{intervention.assigned_to}</td>
            <td>{intervention.notes}</td>
            <td>{intervention.created_at}</td>
        </tr>
    );
}
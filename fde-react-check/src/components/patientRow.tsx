import type {Encounter} from "../types";

export function patientRow({ encounter }: { encounter: Encounter }) {
    return (
        <tr>
            <td>{encounter.encounter_id}</td>
            <td>{encounter.patient_nbr}</td>
            <td>{encounter.age}</td>
            <td>{encounter.risk_level}</td>
            <td>{encounter.risk_score}</td>
        </tr>
    );
}
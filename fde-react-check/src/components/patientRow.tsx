import { Link } from "react-router-dom";
import type {Encounter} from "../types";

export function patientRow({ encounter }: { encounter: Encounter }) {
    return (
        <tr>
            <td>{encounter.encounter_id}</td>
            <td><Link to={`/patients/${encounter.patient_nbr}`}>{encounter.patient_nbr}</Link></td>
            <td>{encounter.age}</td>
            <td>{encounter.risk_level}</td>
            <td>{encounter.risk_score}</td>
            <td>{encounter.readmitted}</td>
        </tr>
    );
}
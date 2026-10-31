import type { Encounter } from "../types";
import { patientRow } from "./patientRow";

interface PatientTableProps {
  encounters: Encounter[];
  onNext: () => void;
  onPrevious: () => void;
  hasNext: boolean;
  hasPrevious: boolean;
}

export function patientTable({ encounters, onNext, onPrevious, hasNext, hasPrevious }: PatientTableProps) {
    return(
      <div>
        <table>
        <thead>
          <tr>
            <th>Encounter ID</th>
            <th>Patient Number</th>
            <th>Age</th>
            <th>Risk Level</th>
            <th>Risk Score</th>
            <th>Readmitted</th>
          </tr>
        </thead>
        <tbody>
          {encounters.map((encounter) => (
            patientRow({ encounter })
          ))}
        </tbody>
      </table>
      {hasPrevious && <button onClick={onPrevious} disabled={!hasPrevious}>PREVIOUS</button>}
      {hasNext && <button onClick={onNext} disabled={!hasNext}>NEXT</button>}
      </div>
    );
}
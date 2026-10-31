import { useState, type SubmitEvent } from 'react';
import type { RiskLevel, SearchCriteria } from '../types';

interface SearchFormProps {
  onSearch: (criteria: SearchCriteria) => void;
  loading: boolean;
}

export function SearchForm({ onSearch, loading }: SearchFormProps) {
  const [patientNumber, setPatientNumber] = useState('');
  const [riskLevel, setRiskLevel] = useState<RiskLevel | ''>('');
  const [riskScore, setRiskScore] = useState('');

  const handleSubmit = (event: SubmitEvent<HTMLFormElement>) => {
    event.preventDefault();
    const score = parseFloat(riskScore);
    onSearch({
      patientNumber: patientNumber.trim() || undefined,
      riskLevel: riskLevel || undefined,
      riskScore: Number.isFinite(score) ? score : undefined,
    });
  };

  const handleClear = () => {
    setPatientNumber('');
    setRiskLevel('');
    setRiskScore('');
    onSearch({});
  };

  return (
    <section className="search-section">
      <h2>Search for a Patient</h2>
      <form onSubmit={handleSubmit}>
        <div className="field">
          <label htmlFor="patientId">Patient ID:</label>
          <input
            type="text"
            id="patientId"
            value={patientNumber}
            onChange={(e) => setPatientNumber(e.target.value)}
          />
        </div>
        <div className="field">
          <label htmlFor="riskLevel">Risk Level:</label>
          <select
            id="riskLevel"
            value={riskLevel}
            onChange={(e) => setRiskLevel(e.target.value as RiskLevel | '')}
          >
            <option value="">Select Risk Level</option>
            <option value="LOW">Low</option>
            <option value="MEDIUM">Medium</option>
            <option value="HIGH">High</option>
          </select>
        </div>
        <div className="field">
          <label htmlFor="riskScore">Risk Score:</label>
          <input
            type="number"
            step="any"
            id="riskScore"
            value={riskScore}
            onChange={(e) => setRiskScore(e.target.value)}
          />
        </div>
        <div className="field">
          <button type="submit" disabled={loading}>Search</button>
          <button type="button" onClick={handleClear} disabled={loading}>Clear</button>
        </div>
      </form>
    </section>
  );
}

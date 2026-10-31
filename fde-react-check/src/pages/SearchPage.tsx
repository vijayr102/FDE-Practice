import { useEffect, useState } from 'react';
import type { Encounter, SearchCriteria } from '../types';
import { SearchForm } from '../components/search';
import { patientTable } from '../components/patientTable';
import { hasCriteria, searchPatients } from '../api';

export function SearchPage() {
  const [encounters, setEncounters] = useState<Encounter[]>([]);
  const [criteria, setCriteria] = useState<SearchCriteria | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = (next: SearchCriteria) => {
  setError(null);
  if (hasCriteria(next)) {
    setCriteria(next);
  } else {            // Clear was pressed
    setCriteria(null);
    setEncounters([]);
  }
};

  useEffect(() => {
    if (!criteria) return;            // nothing searched yet: do nothing
    searchPatients(criteria).then(setEncounters);
  }, [criteria]);                     // runs when the user searches

  return (
    <>
      <SearchForm onSearch={handleSearch} loading={false} />
      {error && <p role="alert">{error}</p>}
      {!error && !encounters.length && <p>Loading...</p>}
      {patientTable({ encounters, hasNext: false, hasPrevious: false, onNext: () => {}, onPrevious: () => {} })}
    </>
  );
}

import { useEffect, useState } from 'react';
import {  fetchEncounters } from '../api';
import type { Encounter } from '../types';
import { patientTable } from '../components/patientTable';

export function AllPatientsPage() {
  const [encounters, setEncounters] = useState<Encounter[]>([]);
  const [offset, setOffset] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const PAGE_SIZE = 10;

  useEffect(() => {
    const controller = new AbortController();
    fetchEncounters(offset, PAGE_SIZE, controller.signal)
      .then((data) => {
        setEncounters(data);
        setError(null);
      })
      .catch((err) => {
        if (controller.signal.aborted) return; // a newer request replaced this one
        console.error('Error fetching encounters:', err);
        setError(String(err));
        setEncounters([]);
      });
    return () => {
      controller.abort();
    };
  }, [offset]);
  const handleNext = () => setOffset((prev) => prev + PAGE_SIZE);
  const handlePrevious = () => setOffset((prev) => Math.max(0, prev - PAGE_SIZE));

  return (
    <div className="App">
        <h2>All Patients</h2>
      {error && <p role="alert">Could not load patients: {error}</p>}
      {!error && encounters.length === 0 && <p>No patients found.</p>}
      {patientTable({
        encounters,
        onNext: handleNext,
        onPrevious: handlePrevious,
        // search results come back in one list, so paging only applies to the unfiltered view
        hasPrevious: offset > 0,
        hasNext:  encounters.length === PAGE_SIZE, // a short page means it's the last one
      })}
    </div>
  );
}

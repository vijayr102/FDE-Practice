import './App.css';
import { header }  from './components/header';
// import type { Encounter, SearchCriteria } from './types';
// import { patientTable } from './components/patientTable';
// import { SearchForm } from './components/search';
// import { API_BASE, hasCriteria, searchPatients } from './api';
// import { useEffect, useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import { AllPatientsPage } from './pages/AllPatientsPage';
import { SearchPage } from './pages/SearchPage';
import { PatientDetails } from './pages/PatientDetails';

function App() {
  return (
    <div className="App">
      {header()}
      <Routes>
        <Route path="/" element={<AllPatientsPage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/patients/:patientId" element={<PatientDetails />} />
      </Routes>
    </div>
  );
}


// function App() {
//   const [encounters, setEncounters] = useState<Encounter[]>([]);
//   const [offset, setOffset] = useState(0);
//   const [criteria, setCriteria] = useState<SearchCriteria>({});
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState<string | null>(null);
//   const PAGE_SIZE = 10;
//   const isSearching = hasCriteria(criteria);

//   useEffect(() => {
//     const controller = new AbortController();

//     async function fetchEncounters(offset: number = 0, limit: number = 10) {
//       const response = await fetch(`${API_BASE}/encounters?limit=${limit}&offset=${offset}`, { signal: controller.signal });
//       if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//       }
//       const data: Encounter[] = await response.json();
//       return data;
//     }

//     async function load() {
//       setLoading(true);
//       setError(null);
//       try {
//         const data = hasCriteria(criteria)
//           ? await searchPatients(criteria, controller.signal)
//           : await fetchEncounters(offset, PAGE_SIZE);
//         setEncounters(data);
//       } catch (error) {
//         if (controller.signal.aborted) return; // a newer request replaced this one
//         console.error('Error fetching encounters:', error);
//         setError(error instanceof Error ? error.message : String(error));
//         setEncounters([]);
//       } finally {
//         if (!controller.signal.aborted) setLoading(false);
//       }
//     }

//     load();
//     return () => controller.abort();
//   }, [offset, criteria]); // re-fetch whenever offset or search criteria change

//   const handleNext = () => setOffset((prev) => prev + PAGE_SIZE);
//   const handlePrevious = () => setOffset((prev) => Math.max(0, prev - PAGE_SIZE));
//   const handleSearch = (next: SearchCriteria) => {
//     setCriteria(next);
//     setOffset(0);
//   };

//   return (
//     <div className="App">
//       {header()}
//       <SearchForm onSearch={handleSearch} loading={loading} />
//       {loading && <p>Loading...</p>}
//       {error && <p role="alert">Could not load patients: {error}</p>}
//       {!loading && !error && encounters.length === 0 && <p>No patients found.</p>}
//       {patientTable({
//         encounters,
//         onNext: handleNext,
//         onPrevious: handlePrevious,
//         // search results come back in one list, so paging only applies to the unfiltered view
//         hasPrevious: !isSearching && offset > 0,
//         hasNext: !isSearching && encounters.length === PAGE_SIZE, // a short page means it's the last one
//       })}
//     </div>
//   );
// }

export default App;

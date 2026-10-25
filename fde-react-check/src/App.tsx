import './App.css';
import { header }  from './components/header';
import type { Encounter } from './types';
import { patientTable } from './components/patientTable';
import { useEffect, useState } from 'react';
  

function App() {
  const [encounters, setEncounters] = useState<Encounter[]>([]);
  const [offset, setOffset] = useState(0);
  const PAGE_SIZE = 10;

  useEffect(() => {
    async function fetchEncounters(offset: number = 0, limit: number = 10) {
      try {
        const response = await fetch(`http://127.0.0.1:3003/encounters?limit=${limit}&offset=${offset}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data: Encounter[] = await response.json();
        setEncounters(data);
      } catch (error) {
        console.error('Error fetching encounters:', error);
      }
    }

    fetchEncounters(offset, PAGE_SIZE);
  }, [offset]); // re-fetch whenever offset changes

  const handleNext = () => setOffset((prev) => prev + PAGE_SIZE);
  const handlePrevious = () => setOffset((prev) => Math.max(0, prev - PAGE_SIZE));

  return (
    <div className="App">
      <h1>{header().title}</h1>
      {patientTable({
        encounters,
        onNext: handleNext,
        onPrevious: handlePrevious,
        hasPrevious: offset > 0,
        hasNext: encounters.length === PAGE_SIZE, // a short page means it's the last one
      })}
    </div>
  );
}

export default App;
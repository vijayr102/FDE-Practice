export interface Encounter {
  encounter_id: number
  patient_nbr: number
  age: string
  risk_level: string
  risk_score: number
  readmitted: string
}

export type RiskLevel = 'LOW' | 'MEDIUM' | 'HIGH'

export interface SearchCriteria {
  patientNumber?: string
  riskLevel?: RiskLevel
  riskScore?: number
}

export interface Intervention {
  intervention_id: number
  encounter_id: number
  status: string
  assigned_to: string
  notes: string
  created_at: string
}


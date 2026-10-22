from fastapi import FastAPI
from repository import get_operational_summary, update_intervention_assignee, get_readmission_risk_analysis
from interventionsServices import router as interventions_router
from encountersServices import router as encounters_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",      # Common React/Next.js local port
    "http://127.0.0.1:8000" # Your production domain
]

# 2. Add the CORSMiddleware to your application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows specific origins
    allow_credentials=True,           # Allows cookies, authorization headers, or SSL certs
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, PUT, DELETE, OPTIONS, etc.)
    allow_headers=["*"],              # Allows all standard and custom request headers
)

app.include_router(encounters_router)
app.include_router(interventions_router)

@app.get("/operational-summary")
def get_operational_summary_endpoint():
    summary, status_counts = get_operational_summary()
    return {**summary,**status_counts}

@app.get("/readmission-risk-analysis")
def get_readmission_risk_analysis_endpoint():
    # Implement the logic for readmission risk analysis
    return get_readmission_risk_analysis()

@app.get("/executive-summary")
def get_executive_summary():
    summary, status_counts = get_operational_summary()
    readmission_risk_analysis = get_readmission_risk_analysis()
    
    return {
        "operational_summary": summary,
        "status_counts": status_counts,
        "readmission_risk_analysis": readmission_risk_analysis
    }
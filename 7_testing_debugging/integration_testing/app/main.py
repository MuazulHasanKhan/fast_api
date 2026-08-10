from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.logic import is_eligible_for_loan

app = FastAPI()

class Applicant(BaseModel):
    income: float = Field(..., gt=0, description="Applicant's income")
    age: int = Field(..., gt=0, description="Applicant's age")
    employment_status: str = Field(..., description="Applicant's employment status")

@app.post("/loan_eligibility")
def check_loan_eligibility(applicant: Applicant): # route handler function that takes an Applicant object as input
    eligible = is_eligible_for_loan(
        income=applicant.income,
        age=applicant.age,
        employment_status=applicant.employment_status
    )
    return {"eligible": eligible}

# This is where the API is defined, exposing endpoints for the end user
# Denotes the entry point for the API server
# Defines the endpoints and their corresponding request handler
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas, crud
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

# create dependency with the database
def get_db():
    db = SessionLocal()
    try:
        yield db # generator
    finally:
        db.close()

# endpoints
# 1. create an employee
@app.post("/employees", response_model = schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db = db, employee = employee)

# 2. get all employees
@app.get("/employees", response_model = List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db = db)

# 3. get employee by id
@app.get("/employees/{employee_id}", response_model = schemas.EmployeeOut)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db = db, employee_id = employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


# 4. update employee by id
@app.put("/employees/{employee_id}", response_model = schemas.EmployeeOut)
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db = db, employee_id = employee_id, employee = employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#5. delete employee by id
@app.delete("/employees/{employee_id}", response_model = dict)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db = db, employee_id = employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully" }
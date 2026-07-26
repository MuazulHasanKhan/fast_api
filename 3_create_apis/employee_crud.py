from fastapi import FastAPI, HTTPException
from model_val import employee
from typing import List
 


#Implementation of CRUD operations for employee management
# 1. Show all employees
# 2. Show particular employee
# 3. Add new employee
# 4.Update employee details
# 5. Delete employee

employees_db: List[employee] = []

app = FastAPI()

#1. Read all employees
@app.get("/employees", response_model = List[employee])
def get_employeed():
    return employees_db


# 2. read particular employee
@app.get('/employees/{emp_id}', response_model = employee)
def get_employee(emp_id:int):
    for idx, emp in enumerate(employees_db):
        if emp.id == emp_id:
            return employees_db[idx] 
    raise HTTPException(status_code=404, detail="Employee not found")




# . Add new employee
@app.post('/employees', response_model = employee)
def add(emp: employee):
    for employee in employees_db:
        if employee.id == emp.id:
            raise HTTPException(status_code=400, detail="Employee already exists")
    employees_db.append(emp)
    return emp

# 4. Update employee details
@app.put('/employees/{emp_id}', response_model = employee)
def update(emp_id:int, emp: employee): # quite confused woith the second
    for idx, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[idx] = emp
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete('/employees/{emp_id}')
def delete(emp_id:int):
    for idx, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[idx]
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")



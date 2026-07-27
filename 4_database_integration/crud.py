# encapsulates are database opeartions for Employee 
# abstracts away raw database queries from the API routes,keeping the code modular
# keeps db logic separate and reusable, making it easier to maintain and test

from sqlalchemy.orm import Session
import models, schemas

# all operations happens in a database session, which is a temporary workspace for interacting with the database. It allows you to query, add, update, and delete records in a controlled manner. The session ensures that changes are tracked and can be committed or rolled back as needed.
def get_employees(db:Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, employee_id:int):
    return (
        db
        .query(models.Employee)
        .filter(models.Employee.id == employee_id)
        .first()
    )

def create_employee(db:Session, employee:schemas.EmployeeCreate):
    db_employee = models.Employee(name =  employee.name, email = employee.email)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db:Session, employee_id:int, employee:schemas.EmployeeUpdate):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee


def delete_employee(db:Session, employee_id:int):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        db.delete(db_employee)
        db.commit() # theres no point in refreshing the object after deletion, as it no longer exists in the database.  
    return db_employee




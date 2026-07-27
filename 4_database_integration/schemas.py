from pydantic import BaseModel, EmailStr
from typing import Optional


class EmployeeBase(BaseModel):
    name: str # common fileds we determine in base class
    email: EmailStr

# Input for creating a new employee
class EmployeeCreate(EmployeeBase):
    email: Optional[EmailStr]
    pass # id is autogenrated  

#input for updating an existing employee
class EmployeeUpdate(EmployeeBase):
    pass # id cant be updated
#oputput for returning employee data
class EmployeeOut(EmployeeBase):
    id: int

# allows pydantic to read data from SQLAlchemy models and convert it to pydantic model
    class Config: # SQL Alchemy expects
        orm_mode = True






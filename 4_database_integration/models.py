from sqlalchemy import column, Integer, String, Float
from database import Base

class Employee(Base):
    __tablename__ = 'employees'
    id = column(Integer, primary_key=True, index=True)
    name = column(String(50), nullable = False)
    email = column(String(50), unique = True, nullable = False)



    
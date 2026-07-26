from pydantic import BaseModel

class employee(BaseModel):
    id: int
    name: str
    department: str
    age: int
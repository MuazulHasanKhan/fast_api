from pydantic import BaseModel, Field
from typing import Optional
# Using Field we cana add validation to the fields of the model. For example, we can specify that the id field must be greater than 0, and that the name and department fields must have a minimum length of 3 and a maximum length of 50.
class employee(BaseModel):
    id: int = Field(..., gt = 0) #...field is required #greater than 0
    name: str = Field(..., min_length = 3, max_length = 50) #...field is required #min length 1 and max length 50
    department: str = Field(..., min_length = 3, max_length = 50) #...field is required #min length 1 and max length 50
    age: Optional[int] = Field(None, gt = 0) #...field is optional #greater than 0 # Pydantic also does type conversion if we give "35" it trie to convert to integer

# for strings we also have regex validation. For example, we can specify that the name field must only contain letters and spaces, and that the department field must only contain letters and numbers.
# We could use StrictInt for if we dot want auto conversion


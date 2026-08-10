from pydantic import BaseModel, Field

class User(BaseModel):
    username: str 
    password: str 


class UserInDB(User):
    hashed_password: str


# keeps tha classes separate from the main application logic, making it easier to manage and maintain the codebase.
# it also separates what the client sends and what is figured out internally 
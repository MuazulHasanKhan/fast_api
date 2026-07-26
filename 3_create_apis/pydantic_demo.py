from fastapi import FastAPI
from pydantic import BaseModel


# define a blue print for the data to be returned

class User(BaseModel):
    id: int
    name :str


app = FastAPI()

@app.get('/user', response_model = User) # response_model tells fast api to return the data in the format of the User class (for validation)
def get_user():
    return User(id = 1, name = 'John Doe')

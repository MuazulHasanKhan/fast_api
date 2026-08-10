from fastapi import FastAPI, Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer  , OAuth2PasswordRequestForm
from auth import create_access_token, verify_access_token
from models import UserInDB
from utils import get_user, verify_password

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(form_data.password, user['hashed_password']):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user['username']})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users")
def read_users(token: str = Depends(oauth2_scheme)):
    username = verify_access_token(token)
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user['username']}
# This module handles JWT authentication for the FastAPI application.   
# This is he security engine of the application. It provides functions to generate and verify JWT tokens, as well as a dependency to get the current user from the token.
# This is essential for:
# Creating acess tokens after succesful user autentication
# Verifying and decoding access tokens to authorize users accessing protected routes


from time import time
from authlib.jose import JoseError, jwt
from fastapi import HTTPException

#CONSTANTS

SECRET_KEY = "my_secret"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

# functions

def create_access_token(data: dict):
    header = {"alg": ALGORITHM}
    expire = time.time() + ACCESS_TOKEN_EXPIRE_MINUTES * 60
    payload = data.copy()
    payload.update({"exp": expire})
    token = jwt.encode(header, payload, SECRET_KEY)
    return token.decode("utf-8")

def verify_access_token(token: str):
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()  
        username = claims.get('sub')# Validate the claims (e.g., expiration)
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username    
    except JoseError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")


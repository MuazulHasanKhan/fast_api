from  fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI()

# Header is judt the type hint for the header parameter. It is not a function, so it does not need to be called. It is used to specify that the parameter should be extracted from the request headers.

API_KEY = "my-secret-key"

def get_api_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return api_key

@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {"output": "Access Granted"}


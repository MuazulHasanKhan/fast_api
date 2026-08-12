from fastapi import FastAPI,  Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse


app = FastAPI()

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"An error occurred: {str(exc)}"},
    )

@app.get('/exceptions')
def handle_exceptions():
    result = 10 / 0  # This will raise a ZeroDivisionError
    
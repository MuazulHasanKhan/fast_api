from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
import asyncio

app = FastAPI()

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers['X-Process-Time'] = str(process_time)
        return response
        

app.add_middleware(TimerMiddleware)


@app.get("/hello")
async def hello():
    await asyncio.sleep(1)  # Simulate some processing time
    return {"message": "Hello, World!"}
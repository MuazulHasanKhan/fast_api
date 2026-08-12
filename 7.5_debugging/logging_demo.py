import logging
from fastapi import FastAPI

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format = '[%(asctime)s] (line %(lineno)d) %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S' 

    )


@app.get("/")
def debug_route():
    logging.info("Debug route accessed")
    return {'message':'chat logs!'}
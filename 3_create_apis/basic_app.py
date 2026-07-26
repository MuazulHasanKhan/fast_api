from fastapi import FastAPI

app = FastAPI()

@app.get("/") # get route #1
def home(): # function to handled get request #2
    return {'message': 'hello fastapi'} # data sent to the client #3 




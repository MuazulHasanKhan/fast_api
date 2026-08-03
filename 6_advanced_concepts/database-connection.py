from fastapi import FastAPI, Depends

app = FastAPI()

#dependency function to get database connection
def get_db():
    db = {"connection": "Database connection established"}
    try:
        yield db
    finally:
        db.close()



#endpoint
@app.get('/home')
def home(db = Depends(get_db)): # The result of the dependency function is injected
    return {"message": "Welcome to the database connection API"}
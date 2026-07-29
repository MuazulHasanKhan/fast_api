from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome to the House Price Prediction API"}

@app.post("/predict", response_model=OutputSchema)
def predict(input_data: InputSchema):
    prediction = make_prediction(input_data.model_dump()) # model_dump() is used to convert json to dict
    return {"price": round(prediction, 2)}
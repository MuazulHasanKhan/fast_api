from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction, batch_predict

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome to the House Price Prediction API"}

@app.post("/predict", response_model=OutputSchema)
def predict(input_data: InputSchema):
    prediction = make_prediction(input_data.model_dump()) # model_dump() is used to convert json to dict
    return {"price": round(prediction, 2)}


@app.post('/batchpredict', response_model=list[OutputSchema])
def batch_predict(user_inputs: list[InputSchema]):
    predictions = batch_predict([user_input.model_dump() for user_input in user_inputs])
    return [OutputSchema(price=round(prediction, 2)) for prediction in predictions]

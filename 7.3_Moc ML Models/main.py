from fastapi import FastAPI
from pydantic import BaseModel
from model import model

app = FastAPI()

class Data(BaseModel):
    SepalLength: float
    SepalWidth: float
    PetalLength: float

@app.post("/predict")
def predict(data: Data ):
    input_data = [[data.SepalLength, data.SepalWidth, data.PetalLength]]
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])} # this is an numpy.int64 object wich cant be converted

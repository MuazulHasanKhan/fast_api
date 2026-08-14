from fastapi import FastAPI, Request
from pydantic import BaseModel
import redis
import json
import hashlib
import joblib

app = FastAPI()
redis_client =  redis.Redis(host = 'localhost', port = 6379, db = 0)

model = joblib.load('./model.joblib')

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

    def to_list(self):
        return [self.feature1, self.feature2, self.feature3]

    def cache_key(self):
        raw = json.dumps(self.model_dump(), sort_keys=True 
                            )
        return f"Predict: {hashlib.sha256(raw.encode()).hexdigest()}"



@app.post("/predict")
async def predict(input_data: InputData):
    key = input_data.cache_key()
    cached_result = redis_client.get(key)
    if cached_result:
        print("Cache hit!")
        return {"prediction": json.loads(cached_result)}
    else:
        prediction = int(model.predict([input_data.to_list()])[0]) # int is important fastapi cant handle numpy
        redis_client.set(key, json.dumps(prediction), ex = 3600)  # Cache for 1 hour
        return {"prediction": prediction}
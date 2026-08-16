import joblib
import numpy as np


model = joblib.load('linear_regression_model.joblib')
print('loaded the model from disk')

def make_prediction(data:dict)-> float:
    # model expects numpy object, so we need to convert the input data to a numpy array
    input_data = np.array(list(data.values())).reshape(1, -1)
    return model.predict(input_data)[0]

def batch_predict(data: list[dict])-> np.array:
    input_data = np.array([list(d.values()) for d in data])
    return model.predict(input_data)


from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
import model

client = TestClient(app)

def test_predict_with_mock():
    with patch('model.model.predict') as mock_predict:
        mock_predict.return_value = [1]  # Mock the
        payload = {
            "SepalLength": 5.1,
            "SepalWidth": 3.5,
            "PetalLength": 1.4
        }
        response = client.post("/predict", json = payload)
        assert response.status_code == 200
        assert response.json() == {"prediction": 1}
        mock_predict.assert_called_once_with([[5.1, 3.5, 1.4]])

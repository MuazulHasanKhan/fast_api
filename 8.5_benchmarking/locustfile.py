import json
from locust import HttpUser, task, between


# HTTP represents a simulated user making HTTP requests
class APIUser(HttpUser):
    #between used to set wait time  between tasks (to simulate real user behavior)
    wait_time = between(1, 2)  # Simulate user think time between requests

# @task used to mark methods as tasks that locust will execute

    @task
    def call_predict(self):
        payload = {
            'feature1': 1.0,
            'feature2': 2.0
        }
        headers = {'content-type': 'application/json' }
        self.client.post('/predict', data = json.dumps(payload), headers = headers)


    @task(1)
    def call_root(self):
        self.client.get('/')


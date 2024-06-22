import unittest as uni
import json
from app import app


class FlaskTestCase(uni.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_data_roberta(self):
        response = self.app.get("/api/roberta?input=I love this product! It's amazing.")  
        # print(response.get_data(as_text=True))  # Print the response data for debugging
        # Check if response status code is 200
        self.assertEqual(response.status_code, 200, f"Expected 200 OK but got {response.status_code}")
        # Attempt to load the response data as JSON
        try:
            data = json.loads(response.get_data(as_text=True))
        except json.JSONDecodeError as e:
            self.fail(f"Response data is not valid JSON: {e}")

    def test_get_data_distilbert(self):
        response = self.app.get("/api/distilbert?input=I love this product! It's amazing.")  
        # print(response.get_data(as_text=True))  # Print the response data for debugging
        # Check if response status code is 200
        self.assertEqual(response.status_code, 200, f"Expected 200 OK but got {response.status_code}")
        # Attempt to load the response data as JSON
        try:
            data = json.loads(response.get_data(as_text=True))
        except json.JSONDecodeError as e:
            self.fail(f"Response data is not valid JSON: {e}")


if __name__ == '__main__':
    uni.main()
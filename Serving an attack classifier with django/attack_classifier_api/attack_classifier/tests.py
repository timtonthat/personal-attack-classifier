from rest_framework.test import APITestCase
from rest_framework import status


class PredictionTestCase(APITestCase):
    def test_prediction(self):
        text_input = "Fuck you deep shit!"
        data = {"text_input": text_input}
        response = self.client.post("/api/classify_text", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["pred"], 98.41029357910156)
        self.assertEqual(response.data["text_input"], text_input)

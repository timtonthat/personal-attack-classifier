from rest_framework.views import APIView
from rest_framework.response import Response
from tensorflow.python.keras.models import load_model, model_from_json
from rest_framework import status
from tensorflow.python.keras.backend import set_session
import tensorflow as tf


from .text_processing import TextProcessor
from .apps import AttackClassifierConfig


global graph, model

model = "attack_classifier/assets/model_1.json"
weights = "attack_classifier/assets/weights_1.h5"

tf.compat.v1.disable_eager_execution()

sess = tf.compat.v1.Session()
graph = tf.compat.v1.get_default_graph()
set_session(sess)

with open(model, "r") as json_file:
    loaded_model_json = json_file.read()
model = model_from_json(loaded_model_json)
model.load_weights(weights)


class PersonalAttackClassifier(APIView):
    """
    post:
    Return the probability of the given comment to be a personal attack
    """

    def post(self, request, *args, **kwargs):
        if request.data.get("text_input"):
            text_input = request.data.get("text_input")
            line_pad = TextProcessor.process(text_input)
            with graph.as_default():
                set_session(sess)
                pred = model.predict(line_pad)
                prediction = pred[0] * 100
            return Response(
                {"pred": prediction, "text_input": text_input},
                status=status.HTTP_200_OK,
            )

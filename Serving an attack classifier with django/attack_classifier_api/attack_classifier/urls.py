from django.urls import path, include
from django.conf.urls import url
from .views import PersonalAttackClassifier

urlpatterns = [
    path("/classify_text", PersonalAttackClassifier.as_view()),
]

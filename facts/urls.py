from django.urls import path
from . import views

app_name = "mima"
urlpatterns = [
    path('facts/', views.facts, name="facts"),
]

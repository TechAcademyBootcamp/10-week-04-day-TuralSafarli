from django.urls import path
from .views import *

urlpatterns = [
    path('news/', random_news)
]
""" File that imports views from app and sets their paths and named URL """

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
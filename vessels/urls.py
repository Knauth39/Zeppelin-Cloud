# vessels/urls.py

from django.urls import path 

from .views import VesselListView

urlpatterns = [
    path("", VesselListView.as_view(), name="home")
]
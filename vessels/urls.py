# vessels/urls.py

from django.urls import path 

from .views import (
    VesselListView,
    VesselDetailView,
    VesselUpdateView,
    VesselDeleteView,
    VesselCreateView,
)

urlpatterns = [
    path("", VesselListView.as_view(), name="home"),
    path("<int:pk>/", VesselDetailView.as_view(), name="vessel_detail"),
    path("<int:pk>/edit/", VesselUpdateView.as_view(), name="vessel_edit"),
    path("<int:pk>/delete/", VesselDeleteView.as_view(), name="vessel_delete"),
    path("new/", VesselCreateView.as_view(), name="vessel_new"),
]
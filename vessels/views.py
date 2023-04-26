#vessels/views.py
from django.shortcuts import render
from django.views.generic import ListView

from .models import Vessel

class VesselListView(ListView):
    model = Vessel
    template_name = "vessel_list.html"

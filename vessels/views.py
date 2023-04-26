#vessels/views.py
from django.contrib.auth.mixins import (
    LoginRequiredMixin,     # Allows access restricting if logged in / out
    UserPassesTestMixin     # Allows access restricting by specific user
)

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy 

from .models import Vessel

# List of all vessels
class VesselListView(ListView):
    model = Vessel
    template_name = "vessel_list.html"


# Shows details for a Vessel
class VesselDetailView(LoginRequiredMixin, DetailView):
    model = Vessel
    template_name = "vessel_detail.html"

# Updates details for a vessel
class VesselUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vessel
    template_name = "vessel_edit.html"

    # Authenticates user permission to update Article
    # Used by UserPassesTestMixin for logic
    def test_func(self):
        # Variable set to current object (vessel)
        # If admin user on the current obj matches the current user or is a superuser, allow update
        obj = self.get_object()                                                 
        return obj.admin_user == self.request.user or self.request.user.is_superuser 
    
# Deletes Vessel
class VesselDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vessel
    template_name = "vessel_delete.html"
    success_url = reverse_lazy("vessel_list") # Redirects to the list of vessels

    # Authenticates user permission to update Article
    # Used by UserPassesTestMixin for logic
    def test_func(self):
        # Variable set to current object (vessel)
        # If admin user on the current obj matches the current user or is a superuser, allow update
        obj = self.get_object()   
        # TODO - Alter settings for this... how to assign admin in vessel profile?                                                 
        return obj.admin_user == self.request.user or self.request.user.is_superuser 
    
# Creates a NEW Vessel
# Contains custom form_valid for admin setting
class VesselCreateView(LoginRequiredMixin, CreateView):
    model = Vessel 
    template_name = "vessel_new.html"

    # Function to automatically set the admin, to the user that is signed in and create the vessel
    def form_valid(self, form):
        form.instance.admin_user = self.request.user 
        return super().form_valid(form) 
    
# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CusomUserCreationForm


class SignUpView(CreateView):
    form_class = CusomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

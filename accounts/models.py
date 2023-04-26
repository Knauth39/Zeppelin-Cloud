# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Constant variables for User_type
    CAPTAIN         = "Captain"
    YACHT_ADMIN     = "Yacht Admin"
    AGENT           = "Agent"
    MANAGER         = "Manager"

    # Tuple list for User_Type
    LOGIN_TYPE = [
        (CAPTAIN, "Captain"),
        (YACHT_ADMIN, "Yacht Admin"),
        (AGENT, "Agent"),
        (MANAGER, "Manager"),
    ]

    user_type   = models.CharField(max_length=50, choices=LOGIN_TYPE, default=CAPTAIN) 
    company     = models.CharField(max_length=100)  # Either the vessel name, or company name 


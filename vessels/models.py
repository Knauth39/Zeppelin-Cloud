# vessels/models.py

from ast import Attribute
from django.db import models
from django_countries.fields import CountryField
from django.conf import settings 
from django.urls import reverse 
from django.contrib.auth import get_user_model
from attr import attr


# Main Vessel class, with appropriate variables
# "captain" variable should be able to select from a list of Admins set by SuperUser
# Making a CAPTAIN APP may be necessary - as it is to be maintained by the SuperUser..??

class Vessel(models.Model):
    # Constant variables for RIG_TYPE
    MOTOR_YACHT     = "M/Y"
    MOTOR_VESSEL    = "M/V"
    SAILING_YACHT   = "S/Y"
    SAILING_VESSEL  = "S/V"
    TENDER_TO       = "T/T"

    # Tuple List for vessel_type
    RIG_TYPE = [
        (MOTOR_YACHT, "M/Y"),
        (MOTOR_VESSEL, "M/V"),
        (SAILING_YACHT, "S/Y"),
        (SAILING_VESSEL, "S/V"),
        (TENDER_TO, "T/T"),
    ]

    # Vessel data
    # https://pypi.org/project/django-countries/#installation
    thumbnail           = models.ImageField(upload_to='images/', default="yacht_image.jpg")
    vessel_type         = models.CharField(max_length=20, choices=RIG_TYPE, default=MOTOR_YACHT) 
    vessel_name         = models.CharField(max_length=200)
    builder             = models.CharField(max_length=200)
    build_country       = CountryField(max_length=200) 
    year_built          = models.IntegerField(null=True, blank=True)
    flag_country        = CountryField(max_length=200) 
    home_port           = models.CharField(max_length=200)
    owner_name          = models.CharField(max_length=200)
    owner_country       = CountryField(max_length=200) 
    cor_number          = models.CharField(max_length=200)
    cor_expiration      = models.DateField(null=True, blank=True)
    imo_number          = models.IntegerField(null=True, blank=True)
    call_sign           = models.CharField(max_length=200)
    mmsi_number         = models.IntegerField(null=True, blank=True)
    # Vessel sizes
    length_meters       = models.FloatField(null=True, blank=True)
    beam_meters         = models.FloatField(null=True, blank=True)
    draft_meters        = models.FloatField(null=True, blank=True)
    gross_tonnage       = models.IntegerField(null=True, blank=True)
    net_tonnage         = models.IntegerField(null=True, blank=True)
    cbp_decal           = models.IntegerField(null=True, blank=True)
    crusing_permit      = models.IntegerField(null=True, blank=True)
    cruising_permit_exp = models.DateField(null=True, blank=True)
    class_society       = models.CharField(max_length=200)
    engine_make         = models.CharField(max_length=200)
    engine_hp           = models.IntegerField(null=True, blank=True)
    # gross_tonnage => 300
    cofr_number         = models.IntegerField(null=True, blank=True)
    cofr_exp            = models.DateField(null=True, blank=True)
    # if gross_tonnage => 400
    ntvrp_number        = models.IntegerField(null=True, blank=True)
    ntvrp_exp           = models.DateField(null=True, blank=True)
    is_ism              = models.BooleanField(default=False)
    for_charter         = models.BooleanField(default=False)
    notes               = models.TextField(blank=True)
    
    #Function to convert meters to feet
    '''
    def metersToFeet(self):
        CONVERT_NUM = 3.281
        feet = self * CONVERT_NUM
        #return feet 
        
    @attr
    def length_to_feet(self):
        return metersToFeet(self.length_meters)
    
    @attr
    def beam_to_feet(self):
        return metersToFeet(self.beam_meters)
    
    @attr
    def draft_to_feet(self):
        return metersToFeet(self.draft_meters)
    '''
   
    
    # Associate a Captain from the database with the vessel
    # captain = models.ForeignKey(Crew, on_delete=models.CASCADE)

    
    # To view model as a string in admin area
    def __str__(self):
        return self.name_vessle

    # Object editing page will have a "view on site" link that jumps directly to the objects public view
    '''
    def get_absolute_url(self):
        return reverse("yacht_detail", kwargs={"pk": self.pk})
    '''


# Document Class - objects belongling to One Vessel - many to one
'''
MK: May be a good idea to make Document into an App.  
When in the vessel profile, there should be an option to upload their vessel's documents.
'''

# Constant variables for document types
CERT_OF_REGISTRY    = "Certificate of Registry"
CERT_OF_CLASS       = "Certificate of Class"
NTVRP               = "NTVRP"
COFR                = "COFR"
LOAD_LINE           = "Load Line Cert"
US_CRUISING_LICENSE = "US Cruising License"
CREW_LIST           = "Crew List"
OTHER               = "Other"

DOC_TYPE = [
    (CERT_OF_REGISTRY, "Registration"),
    (CERT_OF_CLASS, "Certificate of Class"),
    (NTVRP, "NTVRP"),
    (COFR, "COFR"),
    (LOAD_LINE, "Load Line Certificate"),
    (US_CRUISING_LICENSE, "US Cruising License"),
    (CREW_LIST, "Crew List"),
    (OTHER, "Other"),
]

# This class produces an error 'django.db.utils.OperationalError: table "new__vessels_document" has more than one primary key'
'''
class Document(models.Model):
    document_type   = models.CharField(max_length=25, choices=DOC_TYPE, default=CERT_OF_REGISTRY) 
    #FIXME django.db.utils.OperationalError: table "new__vessels_document" has more than one primary key
    vessel          = models.ForeignKey(Vessel, on_delete=models.CASCADE)    # One-to-Many relationship
    document        = models.FileField(upload_to='files/', null=True)
    # TODO - how to name the file in the database 'name_vessel.document_type'
    def __str__(self):
        return self.document_type
    # FIXME - when attempting to upload a document, error message received:
    # 'no such column: vessels_document.id'
'''

'''
The below listed functions are to be implimented during progress
They require further research 
Seperating them into a different APP may be a better approach

        # Read document data and assign to appropriate variables
        # Impliment PyMuPDF for this function?
        def scanDoc(self):
            type_document = 
            authority_issue =
            date_issue =
            date_expiration =

        def makeDoc(self):
            pass
            
        # Alerts user that a document is about to expire
        def alertDoc(self):
            time_to_expire = date_expiration - date.now
            alert_notice = "There are ", time_to_expire, " days left until ", type_document, " issued by ", authority_issue, " expires."

            if time_to_expire <= 30
                mailto:info@zephyrsolutions.us # make this an enviroment variable

    # Creates a spreadsheet, allowing user to click and choose crew to add to spreadsheet
    def createCrewList():
        # TODO impliment function to create a crew list from crew objects
        pass
'''
    



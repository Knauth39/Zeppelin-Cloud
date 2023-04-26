from django.test import TestCase
from django.urls import reverse 

from .models import Vessel

class VesselTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.vessel = Vessel.objects.create(
            vessel_name="DawnTreader",
            cor_number="21322",
            year_built="2010",
            length_meters="15",
            beam_meters="5", 
            draft_meters="2", 
            gross_tonnage="10", 
        )

    def test_vessel_content(self):
        self.assertEqual(self.vessel.vessel_name, "DawnTreader")
        self.assertEqual(self.vessel.cor_number, "21322")
        self.assertEqual(self.vessel.year_built, "2010")
        self.assertEqual(self.vessel.length_meters, "15")
        self.assertEqual(self.vessel.beam_meters, "5")
        self.assertEqual(self.vessel.draft_meters, "2")
        self.assertEqual(self.vessel.gross_tonnage, "10")

    def test_vessel_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "21322")
        self.assertTemplateUsed(response, "vessel_list.html")



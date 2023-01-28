from django.test import TestCase
from .models import Studentapp

# Create your tests here.

class StudentappModelTest(TestCase):
    def test_studentapp_model_exists(self):
        studentapp = Studentapp.objects.count()

        self.assertEqual(studentapp,0)

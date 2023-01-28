from django.test import TestCase
from .models import Studentapp

# Create your tests here.

class StudentappModelTest(TestCase):
    def test_studentapp_model_exists(self):
        studentapp = Studentapp.objects.count()

        self.assertEqual(studentapp,0)

    def test_string_rep_of_objects(self):
        
        studentapp = Studentapp.objects.create(
            title="Test Studentapp",
            body="Test Body"
        )

        self.assertEqual(str(studentapp),studentapp.title)

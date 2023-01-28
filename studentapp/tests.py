from django.test import TestCase

# Create your tests here.

class StudentappModelTest(TestCase):
    def test_studentapp_model_exists(self):
        studentapp = Studentapp.objects.all()

        self.assertEqual()

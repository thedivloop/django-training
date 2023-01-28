from django.test import TestCase
from .models import Studentapp
from http import HTTPStatus

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

class HomepageTest(TestCase):
    def setUp(self) -> None:
        Studentapp.objects.create(
            title = "sample post test 1",
            body = "uet mattis eget facilisis ante. Praesent rhoncus enim libero, sit amet rutrum arcu pretium quis. Aenean feugiat mi in lectus blandit, ac dapibus lacus vehicula. Aenean commodo, lectus et dapibus portt"
        )

        Studentapp.objects.create(
            title = "sample post test 2",
            body = "uet mattis eget facilisis ante. Praesent rhoncus enim libero, sit amet rutrum arcu pretium quis. Aenean feugiat mi in lectus blandit, ac dapibus lacus vehicula. Aenean commodo, lectus et dapibus portt"
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response,'posts/index.html')
        self.assertEqual(response.status_code,HTTPStatus.OK)
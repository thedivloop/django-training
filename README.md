# Commands

`$ python3 -m venv env`

`source env/bin/activate`

`pip install django`

`django-admin startproject myproject .`

`python3 manage.py migrate`

`python3 manage.py createsuperuser`

`python3 manage.py runserver`

`python3 manage.py startapp studentapp`

Add our app to settings

```python
INSTALLED_APPS = [
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",
  "studentapp.apps.StudentappConfig",
]
```

Initiate git:

`git init`

Add `.gitignore`:

`code .gitignore`

Add this to `.gitignore`:

```
__pycache__/
*.py[cod]
env/
```

Create the repository on github and then link as below.

`git add .`

`git status`

`git commit -m "Initial commit"`

`git remote add origin git@github.com:thedivloop/django-training.git`

`git push -u origin main`

Add our test to `tests.py`:

```python
from django.test import TestCase

# Create your tests here.

class StudentappModelTest(TestCase):
    def test_studentapp_model_exists(self):
        studentapp = Studentapp.objects.all()

        self.assertEqual(studentapp,[])
```

Run the tests:

`python3 manage.py test`

Create `Studentapp` class:

```python
class Studentapp(models.Model):
    title = models.CharField(max_length=25)
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
```

`python3 manage.py makemigrations`

`python3 manage.py migrate`

Add our import in `tests.py`:

```python
from .models import Studentapp
```

`git push`

`git checkout -b tdd2`

`git push`

`fatal: The current branch tdd2 has no upstream branch.`

`To push the current branch and set the remote as upstream, use`

`   git push --set-upstream origin tdd2`


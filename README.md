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

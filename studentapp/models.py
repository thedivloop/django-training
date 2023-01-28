from django.db import models

# Create your models here.

"""
    class Studentapp
        -id:int
        -title:varchar
        -body:text
        -created_at:datetime
        -modified_at:datetime
"""

class Studentapp(models.Model):
    title = models.CharField(max_length=25)
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
    

from django.db import models

# Create your models here.

class Element(models.Model):
    title=models.CharField(max_length=50,primary_key=True)
    snippet=models.TextField()

def _str_(self):
    return self.title

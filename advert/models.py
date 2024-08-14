from django.db import models

# Create your models here.
class Hobby(models.Model):
    question = models.TextField(max_length=500)
    date_pub = models.DateField('date published')

class Option(models.Model):
    choice = models.TextField(max_length=300)

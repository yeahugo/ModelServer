from django.db import models

# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    create_date = models.DateField()


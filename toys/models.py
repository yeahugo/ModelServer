from django.db import models

# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=200)
    thumbnail_url = models.ImageField(upload_to='toys')
    image_url = models.ImageField(upload_to='toys')
    create_date = models.DateField()


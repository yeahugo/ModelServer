#from django.db import models
from mongoengine import *
from ModelServer.settings import DBNAME


# Create your models here.
#class Model(models.Model):
#    name = models.CharField(max_length=200)
#    thumbnail_url = models.ImageField(upload_to='toys')
#    image_url = models.ImageField(upload_to='toys')
#    create_date = models.DateField()

class Toy(Document):
    name = StringField(max_length=200)
    thumbnail = ListField(ImageField())
    image = ListField(ImageField())
    create_date = DateTimeField()

#    meta = {
#        'allow_inheritance': True
#        'indexes':[
#            'name',('+thumbnail')
#        ]
#    }

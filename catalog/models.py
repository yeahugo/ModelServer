#from django.db import models
from mongoengine import *

class Catalog(Document):
    name = StringField(max_length=200)

# Create your models here.

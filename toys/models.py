#from django.db import models
from mongoengine import *
from ModelServer.settings import DBNAME
from catalog.models import Catalog

# Create your models here.
#class Model(models.Model):
#    name = models.CharField(max_length=200)
#    thumbnail_url = models.ImageField(upload_to='toys')
#    image_url = models.ImageField(upload_to='toys')
#    create_date = models.DateField()

class EmImage(EmbeddedDocument):
#    image = db.ReferenceField(Image)
    name = StringField(max_length=200)
    image = ImageField(thumbnail_size=(100,100,True))

class EmFile(EmbeddedDocument):
#    gcodeFile = db.ReferenceField(File)
    name = StringField(max_length=200)
    data = FileField()

class Toy(Document):
    name = StringField(max_length = 200)
    thumbnail = ListField(EmbeddedDocumentField(EmImage))
    images = ListField(EmbeddedDocumentField(EmImage))
    gcode = ListField(EmbeddedDocumentField(EmFile))
    catalog = ReferenceField(Catalog)
    object_size = StringField(max_length = 200)
    file_size = StringField(max_length = 200)
    parts_num = StringField(max_length = 10)
    description = StringField(max_length = 200000)

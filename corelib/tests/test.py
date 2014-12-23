import json
from django.test import TestCase, Client
from toy.models import Toy
from catalog.models import Catalog

class ModelServerTestCase(TestCase):
    def setUp(self):
        Toy.drop_collection()
        Catalog.drop_collection()
        client = Client()
        self.client = client

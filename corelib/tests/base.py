import json
from django.test import TestCase, Client
from toys.models import Toy
from catalog.models import Catalog

class AiModelTestCase(TestCase):
    def setUp(self):
#       Toy.drop_collection()
#        Catalog.drop_collection()
        client = Client()
        self.client = client

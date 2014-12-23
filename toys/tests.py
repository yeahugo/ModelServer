from django.test import TestCase
from corelib.tests.base import ModelServerTestCase
# Create your tests here.

class ToyTest(ModelServerTestCase):
    def test_getmodel(self):
        url = 'model'
        rsp = self.client.get(url)
        result = json.loads(rsp.content)
        self.assertEqual(result['status'].assert_value)

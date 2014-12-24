from django.test import TestCase
from corelib.tests.base import AiModelTestCase
import json
# Create your tests here.

status_success = 200

class ToyTest(AiModelTestCase):
    def test_getmodel(self):
        url = '/models/'
        rsp = self.client.get(url)
        print self.client.get(url)
        print "result code "+str(rsp.status_code)
        print rsp.content
        result = json.loads(rsp.content)
        self.assertEqual(rsp.status_code,status_success)

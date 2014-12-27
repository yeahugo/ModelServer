# coding: utf-8
import json
from django.http import HttpResponse
import corelib.protocol as PC

class JsonResponse(HttpResponse):
    def __init__(self,data={}, err_code=200, content_type="application/json"):
        msg = PC.ERROR_CODE_MSG.get(err_code)
        self.result = {}
        self.result[PC.PCMSG] = msg
        self.result[PC.PCST] = err_code
        self.result[PC.PCDATA] = data
        content = json.dumps(self.result)
        HttpResponse.__init__(self, content=content,content_type=content_type)

    @staticmethod
    def to_json(self):
        return self.result


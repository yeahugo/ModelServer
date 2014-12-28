from django.http import HttpResponse
from toys.models import Toy
import json
import toys.views
from bson.json_util import loads

def get_Oid(file_object):
    file_dict = loads(file_object.to_json())
    file_object = file_dict.values()[0]
    return str(file_object)


def image(request,oid,name):
    toy = Toy.objects(pk=oid).first()
    for image in toy.images:
        if get_Oid(image) == name:
            return HttpResponse(image.image.read(),
                        content_type=image.image.content_type,
                        )

def thumbnail(request,oid,name):
    toy = Toy.objects(pk=oid).first()
    for image in toy.thumbnail:
        if get_Oid(image) == name:
            return HttpResponse(image.image.read(),
                        content_type=image.image.content_type,
                        )
def gcode(request,oid,name):
    toy = Toy.objects(pk=oid).first()
    for gcode_file in toy.gcode:
        print gcode_file.data
        if get_Oid(gcode_file) == name:
            return HttpResponse(gcode_file.data.read(),
                        content_type=gcode_file.data.content_type,
                        )


from django.http import HttpResponse
from toys.models import Toy
import json

def image(request,oid,name):
    toy = Toy.objects(pk=oid).first()
    for image in toy.images:
        if str(image.image.name) == name:
            return HttpResponse(image.image.read(),
                        content_type=image.image.content_type,
                        )

def thumbnail(request,oid,name):
    toy = Toy.objects(pk=oid).first()
    for image in toy.thumbnail:
        if str(image.image.name) == name:
            return HttpResponse(image.image.read(),
                        content_type=image.image.content_type,
                        )
def gcode(request,oid,name):
    toy = Toy.objects(pk=oid).first()
    for gcode_file in toy.gcode:
        print gcode_file.data
        if str(gcode_file.data.name) == name:
            return HttpResponse(gcode_file.data.read(),
                        content_type=gcode_file.data.content_type,
                        )


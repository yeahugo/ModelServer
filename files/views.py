from django.http import HttpResponse
from toys.models import Toy
import json

def image(request,oid,name):
    toy = Toy.objects(pk=oid).first()
    for image in toy.images:
        print image.image.name
        print name
        if str(image.image.name) == name:
            return HttpResponse(image.image.read(),
                        content_type=image.image.content_type,
                        )
def thumbnail(request,oid,name):
    toy = Toy.objects(pk=oid).first()
    for image in toy.thumbnail:
        print image.image.name
        print name
        if str(image.image.name) == name:
            return HttpResponse(image.image.read(),
                        content_type=image.image.content_type,
                        )

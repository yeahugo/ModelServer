from django.http import HttpResponse
from toys.models import Toy
from django.core import serializers
import json

# Create your views here.
def index(request):
#    print Toy.objects.all()
#    data = serializers.serialize("json",Toy.objects.all())
    data = Toy.objects.to_json()
    for toy in Toy.objects:
        print toy.id
#       print toy.thumbnail
#       for thumb in toy.thumbnail:
#           image = thumb.image
#           print thumb.image.read()
#    print data
    return HttpResponse(data)

def detail(request,oid):
    toy = Toy.objects(pk=oid).first()
    images = []
    thumbnail = []
    for image in toy.images:
        image_url = "api/image/"+str(toy.id)+"/"+str(image.image.name)
        images.append(image_url)
    for thumb in toy.thumbnail:
        thumbnail_url = "api/thumbnail/"+str(toy.id)+"/"+str(thumb.image.name)
        thumbnail.append(thumbnail_url)
    toyDic = {"name":toy.name,"image":images,"thumbnail":thumbnail}
    toyJson = json.dumps(toyDic)
    print toyJson
    return HttpResponse(toyJson)

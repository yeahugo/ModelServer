from django.http import HttpResponse
from toys.models import Toy
from django.core import serializers
import json

# Create your views here.

def get_thumbnail(toy):
    thumbnails = []
    for thumb in toy.thumbnail:
        thumbnail_url = "api/thumbnail/"+str(toy.id)+"/"+str(thumb.image.name)
        thumbnails.append(thumbnail_url)
    return thumbnails

def index(request):
    toys_json = []
    for toy in Toy.objects.all():
        toy_json = toy.to_json()
        toy_dict = json.loads(toy_json)
        del toy_dict['gcode']
        del toy_dict['images']
        del toy_dict['_id']
        thumbnails = []
        thumbnails = get_thumbnail(toy)
        toy_dict['thumbnail'] = json.dumps(thumbnails)
        toy_dict['id'] = str(toy.id)
        toys_json.append(toy_dict)
    toys_json = json.dumps(toys_json)
    return HttpResponse(toys_json)

def detail(request,oid):
    toy = Toy.objects(pk=oid).first()
    images = []
    thumbnail = []
    gcodes = []
    thumbnail = get_thumbnail(toy)
    for image in toy.images:
        image_url = "api/image/"+str(toy.id)+"/"+str(image.image.name)
        images.append(image_url)
    for gcode in toy.gcode:
        gcode_url = "api/gcode/"+str(toy.id)+"/"+str(gcode.data.name)
        gcodes.append(gcode_url)
    toyDic = {"name":toy.name,"image":images,"thumbnail":thumbnail,
              "gcode":gcodes}
    toyJson = json.dumps(toyDic)
    print toyJson
    return HttpResponse(toyJson)

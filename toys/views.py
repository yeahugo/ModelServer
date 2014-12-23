from django.http import HttpResponse
from toys.models import Toy
from django.core import serializers
import json

# Create your views here.

def get_toy_list(toys):
    toys_json = []
    for toy in toys():
        toy_json = toy.to_json()
        toy_dict = json.loads(toy_json)
        del toy_dict['gcode']
        del toy_dict['images']
        del toy_dict['_id']
        del toy_dict['catalog']
        thumbnails = []
        thumbnails = get_thumbnail(toy)
        toy_dict['thumbnail'] = thumbnails
        toy_dict['id'] = str(toy.id)
        toy_dict['catalog'] = str(toy.catalog.id)
        toys_json.append(toy_dict)
    toys_json = json.dumps(toys_json)
    return toys_json

def get_thumbnail(toy):
    thumbnails = []
    for thumb in toy.thumbnail:
        thumbnail_url = "api/thumbnail/"+str(toy.id)+"/"+str(thumb.image.name)
        thumbnails.append(thumbnail_url)
    return thumbnails

def index(request):
    toys_json = get_toy_list(Toy.objects.all())
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
    toyDic = json.loads(toy.to_json())
#    toyDic = {"name":toy.name,"image":images,"thumbnail":thumbnail,  "gcode":gcodes}
    toyDic['images'] = images
#    toyDic['images'] = json.dumps(images)
    toyDic['thumbnail'] = thumbnail
    toyDic['gcode'] = gcodes
    toyDic['catalog'] = str(toy.catalog.id)
    del toyDic['_id']
    toyJson = json.dumps(toyDic)
    return HttpResponse(toyJson)

def catalog(request,catalogId):
    print "catalogId is "+catalogId
    toys = Toy.objects(catalog=catalogId).all()
    toys_json = get_toy_list(toys)
    return HttpResponse(toys_json)

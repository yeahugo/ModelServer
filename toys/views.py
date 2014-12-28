from django.http import HttpResponse
from toys.models import Toy
from django.core import serializers
import json
from corelib.json_response import  JsonResponse
from bson.json_util import loads

#from corelib.protocol as PC

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
    return toys_json


def get_Oid(file_object):
    file_dict = loads(file_object.to_json())
    file_object = file_dict.values()[0]
    return str(file_object)

def get_thumbnail(toy):
    thumbnails = []
    for thumb in toy.thumbnail:
        thumbnail_url = "api/thumbnail/"+str(toy.id)+"/"+get_Oid(thumb)
        thumbnails.append(thumbnail_url)
    return thumbnails

def index(request):
    toys_dict = get_toy_list(Toy.objects.all())
    return JsonResponse(toys_dict)

def detail(request,oid):
    toy = Toy.objects(pk=oid).first()
    images = []
    thumbnail = []
    gcodes = []
    thumbnail = get_thumbnail(toy)
    for image in toy.images:
        image_url = "api/image/"+str(toy.id)+"/"+get_Oid(image)
        images.append(image_url)
    for gcode in toy.gcode:
        gcode_url = "api/gcode/"+str(toy.id)+"/"+get_Oid(gcode)
        gcodes.append(gcode_url)
    toyDic = json.loads(toy.to_json())
    toyDic['images'] = images
    toyDic['thumbnail'] = thumbnail
    toyDic['gcode'] = gcodes
    toyDic['catalog'] = str(toy.catalog.id)
    del toyDic['_id']
    return JsonResponse(toyDic)

def catalog(request,catalogId):
    toys = Toy.objects(catalog=catalogId).all()
    toys_dict = get_toy_list(toys)
    return JsonResponse(toys_dict)

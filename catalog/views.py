from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Catalog
import json

# Create your views here.
def model(request,catalogId):
    print request
    print catalogId

def index(request):
    catalogs = Catalog.objects.all()
    catalog_json = []
    for catalog in catalogs:
        cata_json = catalog.to_json()
        cata_dict = json.loads(cata_json)
        del cata_dict['_id']
        cata_dict['id'] = str(catalog.id)
        catalog_json.append(cata_dict)
    catalog_json = json.dumps(catalog_json)
    return HttpResponse(catalog_json)

    print request

from django.shortcuts import render
from django.http import HttpResponse
from toys.models import Toy
from django.core import serializers

# Create your views here.
def index(request):
    print Toy.objects.all()
#    data = serializers.serialize("json",Toy.objects.all())
    data = Toy.objects.to_json()
    print data
    return HttpResponse(data)

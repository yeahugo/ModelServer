from django.shortcuts import render
from django.http import HttpResponse
from toys.models import Toy
from django.core import serializers

# Create your views here.
def index(request):
    data = serializers.serialize("json",Toy.objects.all())
    print data
    return HttpResponse(data)

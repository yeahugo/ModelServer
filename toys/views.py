from django.shortcuts import render
from django.http import HttpResponse
from toys.models import Model
from django.core import serializers

# Create your views here.
def index(request):
    data = serializers.serialize("json",Model.objects.all())
    print data
    return HttpResponse(data)

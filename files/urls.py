from django.conf.urls import url
from files import views

urlpatterns = [
    url(r'^image/(\w+)/(.+)',views.image),
    url(r'^thumbnail/(\w+)/(.+)',views.thumbnail),
]

from django.conf.urls import url

from toys import views
from toys import files

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'(\w+)$',views.detail),
    url(r'^image/(\w+)',files.image),
#url(r'thumbnail/\w+',files.thumbnail),
]

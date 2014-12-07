from django.conf.urls import url

from toys import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]

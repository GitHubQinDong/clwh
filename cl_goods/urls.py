from django.conf.urls import url
from cl_goods.views import *
urlpatterns = [
    url(r'^list_(\d+)_(\d+)_(\d+)$', typelist),
    url(r'^(\d+)$', detail),
    url(r'^$', index, name='index'),
]

from django.conf.urls import url
from .views import findItemsByProduct

urlpatterns = [
    # url(r'^$', get, name='list'),
    url(r'^$', findItemsByProduct, name='findItemsByProduct'),
]

from django.urls import path

from herois.views import UniversoCreate, UniversoListViewset, HeroiCreate, UniversoViewSet, HeroiListViewSet, HeroiViewSet
from core.views import index

app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
]

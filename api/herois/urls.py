from django.urls import path

from herois.views import UniversoCreate, UniversoListViewset, HeroiCreate, UniversoViewSet, HeroiListViewSet, HeroiViewSet

app_name = 'herois'
urlpatterns = [
    path('universos/', UniversoListViewset.as_view()),
    path('cadastra_universo/', UniversoCreate.as_view()),
    path('universo/<pk>', UniversoViewSet.as_view()),
    path('busca_herois/', HeroiListViewSet.as_view()),
    path('cadastra_heroi/', HeroiCreate.as_view()),
    path('<pk>', HeroiViewSet.as_view()),
]

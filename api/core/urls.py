from django.urls import path
from core.views import index, addheroi, favorite

app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
    path('addheroi/', addheroi, name='addheroi'),
    path('favoritar/', favorite, name='favoritar'),
]

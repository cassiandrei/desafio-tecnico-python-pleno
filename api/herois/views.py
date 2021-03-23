from django.shortcuts import render

# Create your views here.
from rest_framework.filters import BaseFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny

from herois.models import Universo, Heroi
from herois.serializers import UniversoSerializer, HeroiSerializer


class UniversoListViewset(ListCreateAPIView, DestroyModelMixin):
    """
        Lista de Universos dos Herois.
    """
    serializer_class = UniversoSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Universo.objects.all()


class UniversoViewSet(RetrieveDestroyAPIView):
    """
                Universo.
        """
    serializer_class = UniversoSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Universo.objects.filter(pk=self.kwargs['pk']).first()


class HeroiListViewSet(ListAPIView):
    """
    Lista de herois com busca
    """
    serializer_class = HeroiSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):
        return Heroi.objects.all()


class HeroiCreate(CreateAPIView):
    """
        Cadastra um novo heroi.
    """
    serializer_class = HeroiSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser]


class HeroiViewSet(RetrieveDestroyAPIView):
    """
            Heroi.
        """
    serializer_class = HeroiSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Heroi.objects.filter(pk=self.kwargs['pk']).first()

from rest_framework.filters import BaseFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView, CreateAPIView, \
    UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny

from herois.models import Universo, Heroi
from herois.serializers import UniversoSerializer, HeroiSerializer


class UniversoListViewset(ListAPIView):
    """
        Lista de Universos dos Herois.
    """
    serializer_class = UniversoSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser]

    def get_queryset(self):
        return Universo.objects.all()


class UniversoCreate(CreateAPIView):
    """
        Cadastra um novo universo.
    """
    serializer_class = UniversoSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser]


class UniversoViewSet(RetrieveUpdateDestroyAPIView):
    """
        Universo.
    """
    serializer_class = UniversoSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser]

    def get_queryset(self):
        return Universo.objects.filter(pk=self.kwargs['pk'])


class HeroiListViewSet(ListAPIView):
    """
        Lista de herois com busca.
    """
    serializer_class = HeroiSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser]

    def get_queryset(self, *args, **kwargs):
        return Heroi.objects.all()


class HeroiCreate(CreateAPIView):
    """
        Cadastra um novo heroi.
    """
    serializer_class = HeroiSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser]


class HeroiViewSet(RetrieveUpdateDestroyAPIView):
    """
        Heroi.
    """
    serializer_class = HeroiSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser]

    def get_queryset(self):
        return Heroi.objects.filter(pk=self.kwargs['pk'])

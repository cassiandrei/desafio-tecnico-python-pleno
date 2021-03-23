from rest_framework import serializers

from herois.models import Universo, Heroi


class UniversoSerializer(serializers.ModelSerializer):
    """
     Universo
    """

    class Meta:
        model = Universo
        fields = '__all__'


class HeroiSerializer(serializers.ModelSerializer):
    """
     Heroi
    """

    class Meta:
        model = Heroi
        fields = '__all__'

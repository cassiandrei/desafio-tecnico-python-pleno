from django.db import models

# Create your models here.
from herois.models import Heroi


class Favorito(models.Model):
    heroi = models.ForeignKey(Heroi, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Herói favorito'
        verbose_name_plural = 'Herói favorito'

    def __str__(self):
        return self.heroi.nome

from django.db import models


# Create your models here.
class Universo(models.Model):
    nome = models.CharField('Nome', max_length=50, unique=True)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Universo'
        verbose_name_plural = 'Universos'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Heroi(models.Model):
    nome = models.CharField('Nome', max_length=50)
    foto = models.ImageField('Foto', upload_to='fotos_herois', null=True, blank=True)
    descricao = models.TextField('Descrição')
    universo = models.ForeignKey(Universo, on_delete=models.PROTECT)
    altura = models.FloatField('Altura em metros')
    peso = models.FloatField('Peso em kilos')
    forca = models.FloatField('Força')
    velocidade = models.FloatField('Velocidade')

    class Meta:
        verbose_name = 'Heroi'
        verbose_name_plural = 'Herois'
        ordering = ['universo', 'nome']
        unique_together = ['nome', 'universo']

    def __str__(self):
        return self.nome

    def get_foto_url(self):
        if self.foto:
            return self.foto.url
        else:
            return 'https://isat.com.br/wp-content/uploads/2019/02/Artigo-Jornada-do-her%C3%B3i-720x480.png'
# Generated by Django 3.1.3 on 2021-03-23 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Universo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Universo',
                'verbose_name_plural': 'Universos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Heroi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('foto', models.ImageField(upload_to='fotos_herois', verbose_name='Foto')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('altura', models.FloatField(verbose_name='Altura em metros')),
                ('peso', models.FloatField(verbose_name='Peso em kilos')),
                ('forca', models.FloatField(verbose_name='Força')),
                ('velocidade', models.FloatField(verbose_name='Velocidade')),
                ('universo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='herois.universo')),
            ],
            options={
                'verbose_name': 'Heroi',
                'verbose_name_plural': 'Herois',
                'ordering': ['universo', 'nome'],
                'unique_together': {('nome', 'universo')},
            },
        ),
    ]
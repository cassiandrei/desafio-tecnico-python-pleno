from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from core.forms import HeroiForm
from core.models import Favorito
from herois.models import Heroi


def index(request):
    q = request.GET.get('q', False)
    if q:
        herois = Heroi.objects.filter(nome__contains=q)
    else:
        herois = Heroi.objects.all()
    context = {
        'herois': herois,
    }
    return render(request, 'core/index.html', context=context)


def addheroi(request):
    form = HeroiForm()
    if request.method == 'POST':
        form = HeroiForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            messages.success(request, '{} adicionado'.format(obj.nome))
            return redirect('core:index')
    context = {
        'form': form
    }
    return render(request, 'core/addheroi.html', context=context)


def favorite(request):
    json_data = {'message': 'Informe um ID de herói válido', 'active': False}
    # if request.user.is_authenticated:
    # POST DATA
    id_heroi = request.POST.get('id_heroi', None)
    heroi = Heroi.objects.filter(id=id_heroi).first()
    if heroi:
        fav = Favorito.objects.filter(heroi=heroi)
        if fav:
            fav.delete()
            json_data['active'] = False
            json_data['message'] = "Favorito removido"
        else:
            Favorito.objects.create(heroi=heroi)
            json_data['message'] = "Favorito adicionado"
            json_data['active'] = True
    # else:
    #     json_data['message'] = 'Necessário autenticar na plataforma'
    return JsonResponse(json_data, status=200)


def my_favorites(request):
    favoritos = Favorito.objects.all()
    context = {'favoritos': favoritos}
    return render(request, 'core/meusfavoritos.html', context=context)

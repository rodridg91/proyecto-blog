from django.shortcuts import render
from .models import Noticia
# Create your views here.

def ListarNoticias(request):
    contexto = {}

    n = Noticia.objects.all()
    contexto['noticias'] = n
    return render(request, 'noticias/listar.html', contexto)

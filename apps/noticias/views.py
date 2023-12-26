from django.shortcuts import render
from .models import Noticia,Categoria
# Create your views here.

def ListarNoticias(request):
    
    contexto = {}
    id_categoria = request.GET.get("id",None)
    orden = request.GET.get("orden")
    antiguedad = request.GET.get("antiguedad")

    cat= Categoria.objects.all().order_by('nombre') #oredena categorias por nombre

    #filtra por categoria
    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Noticia.objects.all() # SELECT * FROM NOTICIAS
        
    #ordenar por antiguedad
    if antiguedad == "asc":
        n = n.order_by('fecha_publicacion')
    elif antiguedad == "desc":
        n = n.order_by('-fecha_publicacion')
        
    #ordenar por titulo
    if orden == "asc":
        n = n.order_by('titulo')
    elif orden == "desc":
        n = n.order_by('-titulo')
    

    contexto['noticias'] = n
    contexto['categorias'] = cat
    
    return render(request, 'noticias/listar.html', contexto)

def DetalleNoticia(request, id):
    contexto = {}

    n = Noticia.objects.get(id = id)
    contexto['noticias'] = n
    return render(request, 'noticias/detalle.html', contexto)

    

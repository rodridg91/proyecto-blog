from django.shortcuts import render
from .models import Noticia,Categoria
# Create your views here.

def ListarNoticias(request):
    contexto = {}
    id_categoria = request.GET.get("id",None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
        
    else:
        n = Noticia.objects.all() # SELECT * FROM NOTICIAS
        
    #filtrar por antigüedad ascendente
    antiguedad_asc = request.GET.get("antiguedad_asc")
    if antiguedad_asc:
        n= Noticia.objects.all().order_by('fecha_publicacion')
    
    #filtrar por antigüedad descendente
    antiguedad_desc = request.GET.get("antiguedad_desc")
    if antiguedad_desc:
        n= Noticia.objects.all().order_by('-fecha_publicacion')
        
    #filtrar por titulo ascendente
    titulo_asc = request.GET.get("titulo_asc")
    if titulo_asc:
        n= Noticia.objects.all().order_by('titulo')
    
    #filtrar por titulo descendente
    titulo_desc = request.GET.get("titulo_desc")
    if titulo_desc:
        n= Noticia.objects.all().order_by('-titulo')
    
    cat= Categoria.objects.all().order_by('nombre') #oredena por nombre
    contexto['noticias'] = n
    contexto['categorias'] = cat
    
    return render(request, 'noticias/listar.html', contexto)

def DetalleNoticia(request, id):
    contexto = {}

    n = Noticia.objects.get(id = id)
    contexto['noticias'] = n
    return render(request, 'noticias/detalle.html', contexto)

    

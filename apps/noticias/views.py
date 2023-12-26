from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia,Categoria,Comentario
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NoticiaForm, ComentarioForm
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
    c = n.comentarios.all()
    

    #Borrar noticia
    if request.method == 'POST' and 'delete_noticia' in request.POST:
        n.delete()
        return redirect('noticias:listar')
    
    #Comentarios
    if request.method == 'POST' and 'add_comentario' in request.POST:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            form.save()
        return redirect('noticias:detalle', id=id)
    else:
        form = ComentarioForm()
        
    contexto = {
        'noticias': n,
        'comentarios': c,
        'form': form,
    }


    return render(request, 'noticias/detalle.html', contexto)

@login_required
def AddNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST or None, request.FILES) ##Request files es para las imagenes

        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            form.save()
            return redirect('noticias:listar')
    else:
        form = NoticiaForm()
    
    return render (request, 'noticias/addNoticia.html', {'form':form})

@login_required
def AddComentario(request, noticia_id):


    noticia = get_object_or_404(Noticia, id = noticia_id)  
    if request.method == 'POST':
        contenido = request.POST.get("contenido")
        usuario = request.user.username
        # creacion de comentario
        Comentario.objects.create(noticia = noticia, usuario = usuario, contenido = contenido)
        
    return redirect('noticias:detalle', id = noticia_id)

@login_required
def BorrarComentario(request, comentario_id):


    comentario = get_object_or_404(Comentario, id = comentario_id)  
    if comentario.usuario == request.user.username:
        comentario.delete()
        
    return redirect('noticias:detalle', id = comentario.noticia.id)

@login_required
def EditarNoticia(request, pk):
    noticia = get_object_or_404(Noticia, id=pk)


    # Solo el autor puede editar la noticia
    if noticia.autor != request.user:
        return HttpResponseForbidden("No tenes permiso para editar esta noticia.")


    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias:detalle', id=pk)
    else:
        form = NoticiaForm(instance=noticia)


    context = {
        'form': form,
    }
    return render(request, 'noticias/editar.html', context)

# EDITAR COMENTARIOS
@login_required #debes estar loggeado para poder editar
def EditarComentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)


    # mensaje de error si no sos el autor del comentario
    if comentario.usuario != request.user.username:
        messages.error(request, 'No tenes permiso para editar este comentario')
        return redirect('noticias:detalle', id=comentario.noticia.id)
   
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('noticias:detalle', id=comentario.noticia.id)
    else:
        form = ComentarioForm(instance=comentario)
   
    contexto = {
        'form':form,
        'comentario':comentario,
    }


    return render(request, 'noticias/editar_comentario.html', contexto)

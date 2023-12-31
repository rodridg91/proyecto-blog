from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=50) # = VARCHAR
    resumen = models.CharField(max_length=50, null=True)
    contenido = models.TextField()
    #imagen requiere la libreria pillow
    imagenes = models.ImageField(upload_to='noticias')
    fecha_publicacion = models.DateTimeField(auto_now=True)
    categoria_noticia = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=50)


    def __str__(self):
        return self.contenido


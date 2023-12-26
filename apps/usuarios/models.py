from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Usuario(AbstractUser):
        #imagen de perfil
        imagen = models.ImageField(upload_to='usuarios', default='')
        
        #usuarios del blog y permisos
        USUARIO_COLABORADOR = 'Colaborador'
        USUARIO_VISITANTE = 'Visitante'
        USUARIO_MIEMBRO = 'Miembro'
        USUARIO_SUPER = 'Superusuario'
        
        TIPOS_DE_USUARIO = [
                (USUARIO_COLABORADOR, 'Colaborador'), #is_superuser=False, is_staff=True
                (USUARIO_VISITANTE, 'Visitante'), #no es nada / no aparece en la base de datos
                (USUARIO_MIEMBRO, 'Miembro'), #is_superuser=False, is_staff=False
                (USUARIO_SUPER, 'Superusuario'), #is_superuser=True, is_staff=True
        ]
        tipo_usuario = models.CharField(max_length=20, choices=TIPOS_DE_USUARIO, default=USUARIO_MIEMBRO)
        
        def __str__(self):
                return self.username
        
# Señal para asignar el tipo de usuario "Superusuario" cuando se crea un superusuario
@receiver(post_save, sender=Usuario)
def asignar_tipo_usuario(sender, instance, created, **kwargs):
        if created and instance.is_superuser:
                instance.tipo_usuario = Usuario.USUARIO_SUPER
                instance.save()
                print(f"Usuario {instance.username} es un Superusuario.")




# Señal para asignar el tipo de usuario "Miembro" cuando se crea un usuario
@receiver(post_save, sender=Usuario)
def asignar_miembro(sender, instance, created, **kwargs):
        if created and not instance.is_superuser:
                instance.tipo_usuario = Usuario.USUARIO_MIEMBRO
                instance.save()
                print(f"Usuario {instance.username} es un Miembro.")
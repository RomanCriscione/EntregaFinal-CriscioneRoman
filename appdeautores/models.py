from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Modelo 1: Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo 2: Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo 3: Post (entrada de blog)
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.titulo

# Modelo Perfil
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

# Señales para crear y guardar perfil automáticamente
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()

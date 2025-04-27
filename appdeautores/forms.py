from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from .models import Autor, Categoria, Post, Perfil

# Formulario para crear un autor
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'email']

# Formulario para crear una categoría
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

# Formulario para crear o editar un post
class PostForm(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'autor', 'categoria', 'imagen']

# Formulario para editar el perfil del usuario
class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label='Contraseña nueva', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir la contraseña nueva', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

# Formulario para datos adicionales de perfil
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['bio', 'avatar', 'link']

# Formulario para registrar un nuevo usuario
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
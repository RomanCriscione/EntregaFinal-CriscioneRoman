from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AutorForm, CategoriaForm, PostForm, UserEditForm, PerfilForm, RegistroUsuarioForm
from .models import Post, Autor, Perfil

# Página de inicio
def inicio(request):
    return render(request, 'appdeautores/inicio.html')

# Página principal (Home)
def home(request):
    return render(request, 'appdeautores/home.html')

# Página acerca de mí (About)
def about(request):
    return render(request, 'appdeautores/about.html')

# Crear autor
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorForm()
    return render(request, 'appdeautores/crear_autor.html', {'form': form})

# Crear categoría
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CategoriaForm()
    return render(request, 'appdeautores/crear_categoria.html', {'form': form})

# Listar posts
class PostListView(ListView):
    model = Post
    template_name = 'appdeautores/listar_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

# Ver detalle de un post
class PostDetailView(DetailView):
    model = Post
    template_name = 'appdeautores/detalle_post.html'
    context_object_name = 'post'

# Crear un post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'appdeautores/crear_post.html'
    success_url = reverse_lazy('listar_posts')

# Editar un post
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'appdeautores/editar_post.html', {'form': form})

# Eliminar un post
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('listar_posts')
    return render(request, 'appdeautores/eliminar_post.html', {'post': post})

# Listar autores
def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'appdeautores/listar_autores.html', {'autores': autores})

# Buscar posts por título
def buscar_post(request):
    query = request.GET.get('titulo')
    resultados = []
    if query:
        resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'appdeautores/buscar_post.html', {'resultados': resultados, 'query': query})

# Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'appdeautores/login.html')

# Vista de logout
def logout_view(request):
    logout(request)
    return redirect('inicio')

# Editar perfil
@login_required
def editar_perfil(request):
    user = request.user
    perfil, creado = Perfil.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()

            # Cambiar contraseña si se completaron los campos
            password1 = user_form.cleaned_data.get('password1')
            password2 = user_form.cleaned_data.get('password2')
            if password1 and password1 == password2:
                user.set_password(password1)
                user.save()
                login(request, user)  # Volver a loguear al usuario luego de cambiar la contraseña

            perfil_form.save()
            return redirect('inicio')
    else:
        user_form = UserEditForm(instance=user)
        perfil_form = PerfilForm(instance=perfil)

    return render(request, 'appdeautores/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

# Vista de registro de usuario
def register_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistroUsuarioForm()
    return render(request, 'appdeautores/register.html', {'form': form})
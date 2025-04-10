from django.shortcuts import render, redirect, get_object_or_404
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post, Autor


# Página de inicio
def inicio(request):
    return render(request, 'appdeautores/inicio.html')

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

# Crear post
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')
    else:
        form = PostForm()
    return render(request, 'appdeautores/crear_post.html', {'form': form})

# Listar todos los posts
def listar_posts(request):
    posts = Post.objects.all()
    return render(request, 'appdeautores/listar_posts.html', {'posts': posts})

# Editar post existente
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
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

# Lista Autores

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'appdeautores/listar_autores.html', {'autores': autores})

# Formulario de búsqueda

def buscar_post(request):
    query = request.GET.get('titulo')
    resultados = []
    if query:
        resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'appdeautores/buscar_post.html', {'resultados': resultados, 'query': query})

from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostDetailView, register_view

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('listar-autores/', views.listar_autores, name='listar_autores'),
    path('posts/', PostListView.as_view(), name='listar_posts'),
    path('posts/crear/', PostCreateView.as_view(), name='crear_post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detalle_post'),
    path('posts/editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('posts/eliminar/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
    path('buscar-post/', views.buscar_post, name='buscar_post'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('register/', register_view, name='register'), 
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('posts/', views.listar_posts, name='listar_posts'),
    path('posts/editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('posts/eliminar/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
    path('autores/', views.listar_autores, name='listar_autores'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]

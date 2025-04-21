# libros/urls.py 
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio de libros

     # Libros
    path('libros/', views.LibrosListView.as_view(), name='post_libros'),
    path('libros/detail/<int:pk>/', views.LibrosDetailView.as_view(), name='libros_detail'), # Vista detallada de cada libro
    path('libros/create', views.LibrosCreateView.as_view(), name='libros_create'),  # Crear un nuevo libro
    path('libros/update/<int:pk>/', views.LibrosUpdateView.as_view(), name='libros_update'), # Vista para editar un libro
    path('libros/delete/<int:pk>/', views.LibrosDeleteView.as_view(), name='libros_delete'), # Eliminar un libro

   # Autores    
    path('autores/', views.AutoresListView.as_view(), name='post_autores'),
    path('autores/create', views.AutoresCreateView.as_view(), name='autores_create'),  # Crear un nuevo autor
    path('autores/detail/<int:pk>/', views.AutoresDetailView.as_view(), name='autores_detail'), # Vista detallada de cada autor
    path('autores/update/<int:pk>/', views.AutoresUpdateView.as_view(), name='autores_update'), # Vista para editar un autor
    path('autores/delete/<int:pk>/', views.AutoresDeleteView.as_view(), name='autores_delete'), # Eliminar un autor

    # Reseñas
    path('resenas/', views.post_resenas, name='post_resenas'),
    path('resenas/create', views.resena_create, name='resena_create'),  # Crear una nueva reseña
    path('resenas/create/<int:libro_id>/', views.resena_create, name='resena_create'),
]
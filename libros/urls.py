# libros/urls.py 
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio de libros
    path('about_me/', views.about, name='about_me'),  # Página "Sobre mí"

    ###########################################################################################################################################
    ## Libros
    ###########################################################################################################################################
    path('libros/', views.LibrosListView.as_view(), name='post_libros'),
    path('libros/detail/<int:pk>/', views.LibrosDetailView.as_view(), name='libros_detail'), # Vista detallada de cada libro
    path('libros/create', views.LibrosCreateView.as_view(), name='libros_create'),  # Crear un nuevo libro
    path('libros/update/<int:pk>/', views.LibrosUpdateView.as_view(), name='libros_update'), # Vista para editar un libro
    path('libros/delete/<int:pk>/', views.LibrosDeleteView.as_view(), name='libros_delete'), # Eliminar un libro
   
    ###########################################################################################################################################
    ## Autores
    ###########################################################################################################################################  
    path('autores/', views.AutoresListView.as_view(), name='post_autores'),
    path('autores/create', views.AutoresCreateView.as_view(), name='autores_create'),  # Crear un nuevo autor
    path('autores/detail/<int:pk>/', views.AutoresDetailView.as_view(), name='autores_detail'), # Vista detallada de cada autor
    path('autores/update/<int:pk>/', views.AutoresUpdateView.as_view(), name='autores_update'), # Vista para editar un autor
    path('autores/delete/<int:pk>/', views.AutoresDeleteView.as_view(), name='autores_delete'), # Eliminar un autor

    ###########################################################################################################################################
    ## Reseñas
    ###########################################################################################################################################
    path('resenas/', views.ResenaListView.as_view(), name='post_resenas'), # Listar reseñas
    path('resenas/create/', views.ResenaCreateView.as_view(), name='resena_create'), # Crear una nueva reseña
    path('resenas/create/<int:libro_id>/', views.ResenaCreateView.as_view(), name='resena_create_por_libro'), # Crear una reseña para un libro específico
    path('resenas/<int:pk>/', views.ResenaDetailView.as_view(), name='resena_detail'), # Vista detallada de cada reseña
    path('resenas/update/<int:pk>/', views.ResenaUpdateView.as_view(), name='resena_update'), # Vista para editar una reseña
    path('resenas/delete/<int:pk>/', views.ResenaDeleteView.as_view(), name='resena_delete'), # Eliminar una reseña

    ###########################################################################################################################################
    ## Perfil
    ###########################################################################################################################################
    path('perfil/', views.perfil, name='perfil'), # Vista del perfil del usuario
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'), # Editar perfil del usuario
    path('logout/', views.cerrar_sesion, name='logout'), # Cerrar sesión
    path('login/', views.login_view, name='login'), # Iniciar sesión
    path('registro/', views.registro, name='registro'), # Registro de usuario

]
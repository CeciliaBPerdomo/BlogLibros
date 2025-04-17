# libros/views.py 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, AutorLibro, Resena
from .forms import LibroForm, AutorLibroForm, ResenaForm

# Create your views here.
def index(request):
    return render(request, 'libros/index.html')

###########################################################################################################################################
## Vista libros
def post_libros(request):
    # Obtener el valor de la búsqueda desde la URL
    busqueda = request.GET.get('busqueda', None)
    if busqueda:
        post_libros = Libro.objects.filter(titulo__icontains=busqueda)
    else:
        # Obtener todas las publicaciones de la base de datos
        post_libros = Libro.objects.all()
    return render(request, 'libros/libros.html', context={'libros': post_libros})

def libros_create(request):
    # Lógica para crear un libro
    if request.method == 'POST':
        # Procesar el formulario de creación de publicación
        form = LibroForm(request.POST, request.FILES) 
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect('libros:post_libros')  
            else:
                form.add_error(None, "Debes iniciar sesión para agregar un libro.")
    else:
        form = LibroForm()
    return render(request, 'libros/libros_create.html', context={'form': form})

###########################################################################################################################################
## Vista autores
def post_autores(request):
    # Obtener el valor de la búsqueda desde la URL
    busqueda = request.GET.get('busquedaAutor', None)
    if busqueda:
        post_autores = AutorLibro.objects.filter(nombre__icontains=busqueda)
    else:
        # Obtener todas las publicaciones de la base de datos
        post_autores = AutorLibro.objects.all()
    return render(request, 'libros/autores.html', context={'autores': post_autores})

def autores_create(request):
    # Lógica para crear un libro
    if request.method == 'POST':
        # Procesar el formulario de creación de publicación
        form = AutorLibroForm(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect('libros:post_autores')  
            else:
                form.add_error(None, "Debes iniciar sesión para agregar un autor.")
    else:
        form = AutorLibroForm()
    return render(request, 'libros/autores_create.html', context={'form': form})

###########################################################################################################################################
## Vista reseñas
def post_resenas(request):
    # Obtener el valor de la búsqueda desde la URL
    busqueda = request.GET.get('busquedaResena', None)
    if busqueda:
        post_resenas = Resena.objects.filter(titulo__icontains=busqueda)
    else:
        # Obtener todas las publicaciones de la base de datos
        post_resenas = Resena.objects.all()

     # Preparar las listas de estrellas para cada reseña
    for resena in post_resenas:
        resena.full_stars = [1] * resena.puntuacion
        resena.empty_stars = [1] * (5 - resena.puntuacion)

    return render(request, 'libros/resena.html', context={'resenas': post_resenas})

def resena_create(request, libro_id=None):
    libro = None
    if libro_id:
        libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)

            # Si vino por URL con un libro específico, usar ese
            if libro:
                resena.libro = libro
            resena.usuario = request.user
            resena.save()
            return redirect('libros:post_resenas')
    else:
        form = ResenaForm()

    return render(request, 'libros/resena_create.html', {
        'form': form,
        'libro': libro,
    })
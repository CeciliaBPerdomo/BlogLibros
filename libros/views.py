# libros/views.py 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, AutorLibro, Resena, Avatar
from .forms import LibroForm, AutorLibroForm, ResenaForm, EditUserForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'libros/index.html')

###########################################################################################################################################
## Libros
###########################################################################################################################################

# Vista para mostrar todos los libros o por busqueda realizada
def post_libros(request):
    # Obtener el valor de la búsqueda desde la URL
    busqueda = request.GET.get('busqueda', None)
    if busqueda:
        post_libros = Libro.objects.filter(titulo__icontains=busqueda)
    else:
        # Obtener todas las publicaciones de la base de datos
        post_libros = Libro.objects.all()
    return render(request, 'libros/libros.html', context={'libros': post_libros})

class LibrosListView(ListView):
    model = Libro
    template_name = 'libros/libros.html'
    context_object_name = 'libros'
    ordering = ['-fecha_publicacion']  # Ordenar por fecha de publicación (más reciente primero)

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset


# Vista para mostrar los detalles de un libro
class LibrosDetailView(DetailView):
    model = Libro
    template_name = 'libros/libros_detail.html'

# Vista para crear un nuevo libro
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

class LibrosCreateView(CreateView):
    model = Libro
    template_name = 'libros/libros_create.html'
    form_class = LibroForm
    success_url = reverse_lazy('libros:post_libros')  # Redirigir a la lista de publicaciones después de crear una

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para agregar un libro.")
            return self.form_invalid(form)
        return super().form_valid(form)

# Vista para editar un libro
class LibrosUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/libros_create.html'
    success_url = reverse_lazy('libros:post_libros')  # Redirigir a la lista de publicaciones después de actualizar una

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para agregar un libro.")
            return self.form_invalid(form)
        return super().form_valid(form)

# Vista para eliminar un libro
class LibrosDeleteView(DeleteView):
    model = Libro
    template_name = 'libros/libros_confirm_delete.html'
    success_url = reverse_lazy('libros:post_libros') 

###########################################################################################################################################
## Vista autores
###########################################################################################################################################

# Vista para mostrar todos los autores o por busqueda realizada
def post_autores(request):
    # Obtener el valor de la búsqueda desde la URL
    busqueda = request.GET.get('busquedaAutor', None)
    if busqueda:
        post_autores = AutorLibro.objects.filter(nombre__icontains=busqueda)
    else:
        # Obtener todas las publicaciones de la base de datos
        post_autores = AutorLibro.objects.all()
    return render(request, 'libros/autores.html', context={'autores': post_autores})

class AutoresListView(ListView):
    model = AutorLibro
    template_name = 'libros/autores.html'
    context_object_name = 'autores'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset

# Vista para crear un autor  
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

class AutoresCreateView(CreateView):
    model = AutorLibro
    template_name = 'libros/autores_create.html'
    form_class = AutorLibroForm
    success_url = reverse_lazy('libros:post_autores')  # Redirigir a la lista de publicaciones después de crear una

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para agregar un libro.")
            return self.form_invalid(form)
        return super().form_valid(form)

# Vista para mostrar los detalles de un autor
class AutoresDetailView(DetailView):
    model = AutorLibro
    template_name = 'libros/autores_detail.html'

# Vista para editar un autor
class AutoresUpdateView(UpdateView):
    model = AutorLibro
    form_class = AutorLibroForm
    template_name = 'libros/autores_create.html'
    success_url = reverse_lazy('libros:post_autores')  # Redirigir a la lista de publicaciones después de actualizar una

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para agregar un libro.")
            return self.form_invalid(form)
        return super().form_valid(form)

# Vista para eliminar un autor
class AutoresDeleteView(DeleteView):
    model = AutorLibro
    template_name = 'libros/autores_confirm_delete.html'
    success_url = reverse_lazy('libros:post_autores') 

###########################################################################################################################################
## Vista reseñas
###########################################################################################################################################
# Vista para mostrar todas las reseñas o por busqueda realizada
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

class ResenaListView(ListView):
    model = Resena
    template_name = 'libros/resena.html'
    context_object_name = 'resenas'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busquedaResena', None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        # Agregar estrellas como en la función basada en vista
        for resena in queryset:
            resena.full_stars = [1] * resena.puntuacion
            resena.empty_stars = [1] * (5 - resena.puntuacion)
        return queryset

# Vista para mostrar los detalles de una reseña
class ResenaDetailView(DetailView):
    model = Resena
    template_name = 'libros/resena_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resena = self.get_object()
        context['object'].full_stars = [1] * resena.puntuacion
        context['object'].empty_stars = [1] * (5 - resena.puntuacion)
        return context

# Vista para crear una reseña
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

class ResenaCreateView(CreateView):
    model = Resena
    template_name = 'libros/resena_create.html'
    form_class = ResenaForm
    success_url = reverse_lazy('libros:post_resenas')  # Redirigir a la lista de publicaciones después de crear una

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            print(self.request.user)
            form.instance.usuario = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para agregar una reseña.")
            return self.form_invalid(form)
        return super().form_valid(form)

# Vista para editar una reseña
class ResenaUpdateView(UpdateView):
    model = Resena
    form_class = ResenaForm
    template_name = 'libros/resena_create.html'
    success_url = reverse_lazy('libros:post_resenas')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.usuario = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para actulizar una reseña.")
            return self.form_invalid(form)
        return super().form_valid(form)

# Vista para eliminar una reseña
class ResenaDeleteView(DeleteView):
    model = Resena
    template_name = 'libros/resena_confirm_delete.html'
    success_url = reverse_lazy('libros:post_resenas')

###########################################################################################################################################
## Perfil
###########################################################################################################################################

# Vista para mostrar el perfil del usuario
@login_required
def perfil(request):
    usuario = request.user
    resenas = Resena.objects.filter(usuario=usuario).select_related('libro')
    return render(request, 'libros/perfil.html', {
        'user': usuario,
        'resenas': resenas,
    })

# Vista para editar el perfil del usuario
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None
        
        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else: 
            avatar_form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect('libros:perfil')
    else:   
        form = EditUserForm(instance=request.user)
        if hasattr(request.user, 'avatar'):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()
    return render(request, 'libros/perfil_editar.html', {'form': form, 'avatar_form': avatar_form})

# Vista para cerrar la sesión del perfil del usuario
def cerrar_sesion(request):
    logout(request)
    return redirect('libros:index')
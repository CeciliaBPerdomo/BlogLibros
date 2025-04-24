# libros/views.py 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Libro, AutorLibro, Resena, Avatar, Perfil, Mensaje, Conversacion
from .forms import LibroForm, AutorLibroForm, ResenaForm, EditUserForm, AvatarForm, CustomLoginForm, RegistroUsuarioForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.dateformat import format as date_format

# Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'libros/index.html')

def about(request):
    return render(request, 'libros/about_me.html')

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
@login_required
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

class LibrosCreateView(LoginRequiredMixin, CreateView):
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
class LibrosUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/libros_create.html'
    success_url = reverse_lazy('libros:post_libros')  # Redirigir a la lista de publicaciones después de actualizar una

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Establecer el valor inicial del campo de fecha con el formato correcto para input type="date"
        if self.object.fecha_publicacion:
            form.initial['fecha_publicacion'] = date_format(self.object.fecha_publicacion, 'Y-m-d')
        return form

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para agregar un libro.")
            return self.form_invalid(form)
        return super().form_valid(form)

# Vista para eliminar un libro
class LibrosDeleteView(LoginRequiredMixin, DeleteView):
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
        busqueda = self.request.GET.get('busquedaAutor', None)
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset

# Vista para crear un autor  
@login_required
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

class AutoresCreateView(LoginRequiredMixin, CreateView):
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
class AutoresUpdateView(LoginRequiredMixin, UpdateView):
    model = AutorLibro
    form_class = AutorLibroForm
    template_name = 'libros/autores_create.html'
    success_url = reverse_lazy('libros:post_autores')  # Redirigir a la lista de publicaciones después de actualizar una

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        try:
            autor = self.get_object()  # Obtén el autor a editar
            # Establecer el valor inicial de la fecha de nacimiento en el formato correcto
            form.initial['fecha_nacimiento'] = autor.fecha_nacimiento.strftime('%Y-%m-%d') if autor.fecha_nacimiento else ''
        except AutorLibro.DoesNotExist:
            pass
        return form

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para agregar un libro.")
            return self.form_invalid(form)
        return super().form_valid(form)

# Vista para eliminar un autor
class AutoresDeleteView(LoginRequiredMixin, DeleteView):
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
@login_required
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

class ResenaCreateView(LoginRequiredMixin, CreateView):
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
class ResenaUpdateView(LoginRequiredMixin, UpdateView):
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
class ResenaDeleteView(LoginRequiredMixin, DeleteView):
    model = Resena
    template_name = 'libros/resena_confirm_delete.html'
    success_url = reverse_lazy('libros:post_resenas')

###########################################################################################################################################
## Usuarios
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
            perfil = request.user.perfil
            form.initial['fecha_cumple'] = perfil.fecha_cumple
            form.initial['biografia'] = perfil.biografia
            form.initial['libro_favorito'] = perfil.libro_favorito
        except Perfil.DoesNotExist:
            pass
        
        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None
        
        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else: 
            avatar_form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid() and avatar_form.is_valid():
            # Guardar la información del usuario
            user = form.save()
            
            # Guardar los datos adicionales del perfil
            perfil, creado = Perfil.objects.get_or_create(user=user)
            perfil.fecha_cumple = form.cleaned_data.get('fecha_cumple')
            perfil.biografia = form.cleaned_data.get('biografia')
            perfil.libro_favorito = form.cleaned_data.get('libro_favorito')
            perfil.save()
            
            # Guardar el avatar si está presente
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            
            return redirect('libros:perfil')
    else:
        form = EditUserForm(instance=request.user)

        try:
            perfil = request.user.perfil
            form.initial['fecha_cumple'] = perfil.fecha_cumple.strftime('%Y-%m-%d') if perfil.fecha_cumple else ''
            form.initial['biografia'] = perfil.biografia
            form.initial['libro_favorito'] = perfil.libro_favorito
        except Perfil.DoesNotExist:
            pass
        
        # Buscar el avatar si existe
        if hasattr(request.user, 'avatar'):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()
    return render(request, 'libros/perfil_editar.html', {'form': form, 'avatar_form': avatar_form})

# Vista para cerrar la sesión del perfil del usuario
def cerrar_sesion(request):
    if request.user.is_authenticated:  # Verificar si el usuario está autenticado
        logout(request)
    return redirect('libros:index')

# Vista para loguearse
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirigir a la página principal después del login
    else:
        form = CustomLoginForm()

    return render(request, 'libros/perfil_login.html', {'form': form})

# Registro de usuario
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil vacío si lo estás usando
            Perfil.objects.create(user=user)
            login(request, user)  # inicia sesión automáticamente
            return redirect('index') 
    else:
        form = RegistroUsuarioForm()
    return render(request, 'libros/perfil_registro.html', {'form': form})

###########################################################################################################################################
## Mensajes
###########################################################################################################################################
# Obtener todas las conversaciones donde el usuario está participando
@login_required
def lista_conversaciones(request):
    conversaciones = Conversacion.objects.filter(participantes=request.user)
    return render(request, 'libros/conversaciones_libros.html', {'conversaciones': conversaciones})

# Obtener la conversación y los mensajes asociados
@login_required
def conversacion(request, conversacion_id):
    conversacion = Conversacion.objects.get(id=conversacion_id)
    if request.user not in conversacion.participantes.all():
        return redirect('libros:lista_conversaciones')  # Si el usuario no está en la conversación, redirigir

    mensajes = conversacion.mensajes.all()
    if request.method == 'POST':
        texto = request.POST['mensaje']
        Mensaje.objects.create(conversacion=conversacion, remitente=request.user, texto=texto)
        return redirect('libros:conversacion', conversacion_id=conversacion.id)

    return render(request, 'libros/conversacion.html', {'conversacion': conversacion, 'mensajes': mensajes})

# Crear una nueva conversación con otro usuario
@login_required
def nueva_conversacion(request, usuario_id):
    usuario = User.objects.get(id=usuario_id)
    conversacion = Conversacion.objects.create()
    conversacion.participantes.add(request.user, usuario)
    conversacion.save()
    return redirect('libros:conversacion', conversacion_id=conversacion.id)

@login_required
def seleccionar_usuario_conversacion(request):
    usuarios = User.objects.exclude(id=request.user.id)
    return render(request, 'libros/conversaciones_seleccionar_usuario.html', {'usuarios': usuarios})
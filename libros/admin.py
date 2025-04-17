from django.contrib import admin
from .models import AutorLibro, Libro, Resena

# Personalización de la vista de AutorLibro
@admin.register(AutorLibro)
class AutorLibroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento')
    search_fields = ('nombre',)


# Personalización de la vista de Libro
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor_libro', 'fecha_publicacion', 'portada')
    list_filter = ('autor_libro', 'fecha_publicacion')
    search_fields = ('titulo', 'autor_libro__nombre')

# Personalización de la vista de Resena
@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'usuario', 'puntuacion', 'fecha')
    list_filter = ('puntuacion', 'fecha')
    search_fields = ('libro__titulo', 'usuario__username')
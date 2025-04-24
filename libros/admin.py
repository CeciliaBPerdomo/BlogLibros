from django.contrib import admin
from .models import AutorLibro, Libro, Resena, Avatar, Perfil, Conversacion, Mensaje

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

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_cumple', 'libro_favorito')
    search_fields = ('user__username', 'libro_favorito')


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('user', 'imagen')
    search_fields = ('user__username',)
    list_filter = ('user',)

@admin.register(Conversacion)
class ConversacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'mostrar_participantes', 'creado_en')
    ordering = ('creado_en',)
    list_filter = ('creado_en',)

    def mostrar_participantes(self, obj):
        return ", ".join([usuario.username for usuario in obj.participantes.all()])
    mostrar_participantes.short_description = 'Participantes'

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('id', 'remitente', 'texto', 'creado_en')
    ordering = ('creado_en',)
    list_filter = ('remitente', 'creado_en')
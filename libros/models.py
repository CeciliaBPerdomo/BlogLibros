from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.
###########################################################################################################################################
## Autores
###########################################################################################################################################
class AutorLibro(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

###########################################################################################################################################
## Libros
###########################################################################################################################################
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor_libro = models.ForeignKey(AutorLibro, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='libros/img/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    def promedio_puntuacion(self):
        promedio = self.resenas.aggregate(Avg('puntuacion'))['puntuacion__avg']
        return round(promedio or 0)

###########################################################################################################################################
## Reseñas
###########################################################################################################################################
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    puntuacion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 a 5 estrellas
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} reseñó {self.libro.titulo}'


###########################################################################################################################################
## Perfil de usuario
###########################################################################################################################################
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_cumple = models.DateField(null=True, blank=True)
    biografia = models.TextField(blank=True, max_length=500)
    libro_favorito = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='libros/avatares/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagen}"
    
# Conversación entre dos usuarios o más
class Conversacion(models.Model):
    participantes = models.ManyToManyField(User)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversación entre {', '.join([usuario.username for usuario in self.participantes.all()])}"

# Mensaje dentro de una conversación
class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, related_name='mensajes', on_delete=models.CASCADE)
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.remitente.username} en {self.conversacion}"

    class Meta:
        ordering = ['creado_en']
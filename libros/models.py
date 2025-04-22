from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.
# Autor del libro 
class AutorLibro(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# Libro
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

# Reseña del libro
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    puntuacion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 a 5 estrellas
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} reseñó {self.libro.titulo}'

# Avatar del usuario
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='libros/avatares/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagen}"
from django.test import TestCase
from django.contrib.auth.models import User
from .models import AutorLibro, Libro, Resena, Perfil, Avatar, Conversacion, Mensaje
from datetime import date
from django.core.exceptions import ValidationError

class AutorLibroTestCase(TestCase):

    def setUp(self):
        self.autor = AutorLibro.objects.create(
            nombre='Gabriel García Márquez',
            biografia='Autor colombiano.',
            fecha_nacimiento=date(1927, 3, 6)
        )

    def test_autor_creacion(self):
        autor = AutorLibro.objects.get(nombre='Gabriel García Márquez')
        self.assertEqual(autor.nombre, 'Gabriel García Márquez')
        self.assertEqual(autor.biografia, 'Autor colombiano.')
        self.assertEqual(str(autor), 'Gabriel García Márquez')


class LibroTestCase(TestCase):

    def setUp(self):
        self.autor = AutorLibro.objects.create(
            nombre='Gabriel García Márquez',
            biografia='Autor colombiano.',
            fecha_nacimiento=date(1927, 3, 6)
        )
        self.libro = Libro.objects.create(
            titulo='Cien años de soledad',
            descripcion='Una novela maravillosa.',
            autor_libro=self.autor,
            fecha_publicacion=date(1967, 6, 5)
        )

    def test_libro_creacion(self):
        libro = Libro.objects.get(titulo='Cien años de soledad')
        self.assertEqual(libro.titulo, 'Cien años de soledad')
        self.assertEqual(libro.autor_libro.nombre, 'Gabriel García Márquez')

    def test_promedio_puntuacion_sin_resenas(self):
        libro = self.libro
        self.assertEqual(libro.promedio_puntuacion(), 0)

    def test_promedio_puntuacion_con_resenas(self):
        usuario = User.objects.create_user(username='usuario', password='contraseña')
        resena = Resena.objects.create(
            libro=self.libro,
            usuario=usuario,
            titulo='Excelente libro',
            contenido='Me encantó.',
            puntuacion=5
        )
        libro = self.libro
        self.assertEqual(libro.promedio_puntuacion(), 5)

    def test_str(self):
        self.assertEqual(str(self.libro), 'Cien años de soledad')


class ResenaTestCase(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(username='usuario', password='contraseña')
        self.autor = AutorLibro.objects.create(
            nombre='Gabriel García Márquez',
            biografia='Autor colombiano.',
            fecha_nacimiento=date(1927, 3, 6)
        )
        self.libro = Libro.objects.create(
            titulo='Cien años de soledad',
            descripcion='Una novela maravillosa.',
            autor_libro=self.autor,
            fecha_publicacion=date(1967, 6, 5)
        )

    def test_resena_creacion(self):
        resena = Resena.objects.create(
            libro=self.libro,
            usuario=self.usuario,
            titulo='Excelente libro',
            contenido='Me encantó.',
            puntuacion=5
        )
        self.assertEqual(resena.titulo, 'Excelente libro')
        self.assertEqual(resena.libro.titulo, 'Cien años de soledad')
        self.assertEqual(resena.puntuacion, 5)

    def test_validar_puntuacion_invalida(self):
        with self.assertRaises(ValidationError):
            resena = Resena(
                libro=self.libro,
                usuario=self.usuario,
                titulo='Excelente libro',
                contenido='Me encantó.',
                puntuacion=6  # Fuera de rango (1-5)
            )
            resena.clean()


class PerfilTestCase(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(username='usuario', password='contraseña')
        self.perfil = Perfil.objects.create(
            user=self.usuario,
            fecha_cumple=date(1990, 5, 15),
            biografia='Amante de la lectura.',
            libro_favorito='Cien años de soledad'
        )

    def test_perfil_creacion(self):
        perfil = Perfil.objects.get(user=self.usuario)
        self.assertEqual(perfil.libro_favorito, 'Cien años de soledad')

    def test_str(self):
        self.assertEqual(str(self.perfil), 'Perfil de usuario')


class AvatarTestCase(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(username='usuario', password='contraseña')
        self.avatar = Avatar.objects.create(
            user=self.usuario,
            imagen='libros/avatares/usuario.png'
        )

    def test_avatar_creacion(self):
        avatar = Avatar.objects.get(user=self.usuario)
        self.assertEqual(avatar.imagen, 'libros/avatares/usuario.png')

    def test_str(self):
        self.assertEqual(str(self.avatar), 'usuario - libros/avatares/usuario.png')


class ConversacionTestCase(TestCase):

    def setUp(self):
        self.usuario1 = User.objects.create_user(username='usuario1', password='contraseña')
        self.usuario2 = User.objects.create_user(username='usuario2', password='contraseña')
        self.conversacion = Conversacion.objects.create()
        self.conversacion.participantes.add(self.usuario1, self.usuario2)

    def test_conversacion_creacion(self):
        conversacion = Conversacion.objects.get(id=self.conversacion.id)
        self.assertEqual(conversacion.participantes.count(), 2)

    def test_str(self):
        self.assertEqual(str(self.conversacion), 'Conversación entre usuario1, usuario2')


class MensajeTestCase(TestCase):

    def setUp(self):
        self.usuario1 = User.objects.create_user(username='usuario1', password='contraseña')
        self.usuario2 = User.objects.create_user(username='usuario2', password='contraseña')
        self.conversacion = Conversacion.objects.create()
        self.conversacion.participantes.add(self.usuario1, self.usuario2)
        self.mensaje = Mensaje.objects.create(
            conversacion=self.conversacion,
            remitente=self.usuario1,
            texto='Hola, ¿cómo estás?'
        )

    def test_mensaje_creacion(self):
        mensaje = Mensaje.objects.get(id=self.mensaje.id)
        self.assertEqual(mensaje.texto, 'Hola, ¿cómo estás?')
        self.assertEqual(mensaje.remitente.username, 'usuario1')

    def test_str(self):
        self.assertEqual(str(self.mensaje), 'Mensaje de usuario1 en Conversación entre usuario1, usuario2')

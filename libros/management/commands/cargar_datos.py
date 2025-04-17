from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from libros.models import AutorLibro, Libro, Resena
from datetime import date

# Imagenes de portada
from django.conf import settings
from django.core.files import File
from pathlib import Path

# Rutas de las imágenes para cada libro
media_root = Path(settings.MEDIA_ROOT)  # Aseguramos que la ruta sea un objeto Path
portada_libro1 = media_root / 'libros' / 'img' / 'cien.jpeg'
portada_libro2 = media_root / 'libros' / 'img' / 'orgullo.jpg'
portada_libro3 = media_root / 'libros' / 'img' / 'rosasyespinas.jpg'
portada_libro5 = media_root / 'libros' / 'img' / 'nacida.png'

class Command(BaseCommand):
    help = 'Carga autores, libros y reseñas de ejemplo'

    def handle(self, *args, **kwargs):
        # Crear usuarios
        usuario, _ = User.objects.get_or_create(username='Cecilia', defaults={'password': 'ceci1234'})

        # Crear autores
        autor1, _ = AutorLibro.objects.get_or_create(
            nombre='Gabriel García Márquez',
            defaults={
                'biografia': 'Escritor colombiano, autor de "Cien años de soledad" y premio Nobel de Literatura en 1982.',
                'fecha_nacimiento': date(1927, 3, 6)
            }
        )

        autor2, _ = AutorLibro.objects.get_or_create(
            nombre='Jane Austen',
            defaults={
                'biografia': 'Novelista inglesa del siglo XIX, famosa por su aguda crítica social y obras como "Orgullo y prejuicio".',
                'fecha_nacimiento': date(1775, 12, 16)
            }
        )

        autor3, _ = AutorLibro.objects.get_or_create(
            nombre='Sarah J. Maas',
            defaults={
                'biografia': 'Autora estadounidense de fantasía, conocida por sus sagas "Throne of Glass" y "Una corte de rosas y espinas".',
                'fecha_nacimiento': date(1986, 3, 5)
            }
        )

        autor4, _ = AutorLibro.objects.get_or_create(
            nombre='Jennifer L. Armentrout',
            defaults={
                'biografia': 'Jennifer Lynn Armentrout también conocida por el seudónimo de J. Lynn, es una escritora estadounidense de romance contemporáneo, new adult y fantasía. Varias de sus obras han aparecido en la lista de los más vendidos del The New York Times.',
                'fecha_nacimiento': date(1980, 6, 11)
            }
        )

        # Crear libros
        libro1, _ = Libro.objects.get_or_create(
            titulo='Cien años de soledad',
            descripcion='Una novela emblemática del realismo mágico.',
            autor_libro=autor1,
            fecha_publicacion=date(1967, 5, 30)
        )
        # Asignar portada específica para el libro1
        if portada_libro1.exists():
            with open(portada_libro1, 'rb') as f:
                libro1.portada.save('cien.jpeg', File(f), save=True)

        libro2, _ = Libro.objects.get_or_create(
            titulo='Orgullo y prejuicio',
            descripcion='Orgullo y prejuicio (en inglés, Pride and Prejudice), publicada por primera vez el 28 de enero de 1813 como una obra anónima, es la más famosa de las novelas de Jane Austen y una de las primeras comedias románticas en la historia de la novela. Su primera frase es, además, una de las más famosas en la literatura inglesa: «Es una verdad mundialmente reconocida que un hombre soltero, poseedor de una gran fortuna, necesita una esposa». Es una novela de desarrollo personal, en la que las dos figuras principales, Elizabeth Bennet y Fitzwilliam Darcy, cada uno a su manera y, no obstante, de forma muy parecida, deben madurar para superar algunas crisis y aprender de sus errores para poder encarar el futuro en común, superando el orgullo de clase de Darcy y los prejuicios de Elizabeth hacia él. Es una de las obras más conocidas de la literatura inglesa, gracias a innumerables ediciones y, recientemente, a películas (como Orgullo y prejuicio, 2005), reescrita incluso en forma de un musical de Broadway.',
            autor_libro=autor2,
            fecha_publicacion=date(1813, 1, 28)
        )
        # Asignar portada específica para el libro2
        if portada_libro2.exists():
            with open(portada_libro2, 'rb') as f:
                libro2.portada.save('orgullo.jpg', File(f), save=True)

        libro3, _ = Libro.objects.get_or_create(
            titulo='Una corte de rosas y espinas',
            descripcion='Primer libro de la saga de fantasía romántica donde Feyre descubre un mundo lleno de magia y peligro.',
            autor_libro=autor3,
            fecha_publicacion=date(2015, 5, 5)
        )
        # Asignar portada específica para el libro3
        if portada_libro3.exists():
            with open(portada_libro3, 'rb') as f:
                libro3.portada.save('rosasyespinas.jpg', File(f), save=True)

        libro4, _ = Libro.objects.get_or_create(
            titulo='Obsidian: Saga Lux 1',
            descripcion='Una historia de amor y ciencia ficción llena de misterio y acción.',
            autor_libro=autor4,
            fecha_publicacion=date(2013, 12, 1)
        )

        libro5, _ = Libro.objects.get_or_create(
            titulo='Nacida de sangre y cenizas',
            descripcion='La línea entre el amor y la obsesión nunca ha sido tan amplia... Aunque Sera se ha liberado de las garras de Kolis y ha regresado con sus seres queridos, no todo está en calma. Los recuerdos todavía la atormentan, pero Sera, por fin, tiene esperanza en un futuro con la otra mitad de su corazón y de su alma. Nyktos desea, ama y acepta todas las partes de ella... incluso las más monstruosas. Sera y Ash tienen que luchar por todo lo que hay en los mundos, y Nyktos no tiene ninguna duda de que Sera puede ser la Reina de los Dioses. No obstante, ella debe tener fe en sí misma si quieren convencer a las otras cortes para que los apoyen contra Kolis, y poder hacer así de Iliseeum y del mundo mortal lugares mejores y más seguros para todos.',
            autor_libro=autor4,
            fecha_publicacion=date(2025, 3, 4)
        )

         # Asignar portada específica para el libro3
        if portada_libro5.exists():
            with open(portada_libro5, 'rb') as f:
                libro5.portada.save('nacida.png', File(f), save=True)

        # Crear reseñas
        Resena.objects.get_or_create(
            libro=libro1,
            usuario=usuario,
            titulo='Una obra maestra',
            contenido='Me encantó cada página de este libro. Inolvidable.',
            puntuacion=5
        )

        Resena.objects.get_or_create(
            libro=libro2,
            usuario=usuario,
            titulo='Un clásico imprescindible',
            contenido='La ironía y la crítica social de Austen son brillantes.',
            puntuacion=4
        )

        Resena.objects.get_or_create(
            libro=libro3,
            usuario=usuario,
            titulo='Fantástico y atrapante',
            contenido='Me encantó el mundo que construye Maas. No podía dejar de leer.',
            puntuacion=5
        )

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))

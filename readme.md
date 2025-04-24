<h1 align="center">Mi blog de libros</h1>
<p align="center"><img src="myAvatar.png" width: "40%"></p>
<p align="center">by <b>Cecilia 💛 Perdomo</b></p>

<p align="center">
Este es un proyecto Django para la gestión de libros, autores, reseñas y la interacción entre usuarios mediante mensajes y conversaciones. 
</p>

## Base de datos
- 📘 **Módelo 1**: AutorLibro → Información sobre los autores de los libros que reseñás.
- 📚 **Módelo 2**: Libro → Cada libro tiene un título, descripción, autor, etc.
- ✍️ **Módelo 3**: Reseña → Las reseñas que recibe cada libro.

- Crea la base de datos: `python manage.py migrate`
    - 🧠 Si agregás o modificás un modelo, siempre tenés que correr makemigrations y migrate, así Django sabe qué cambios reflejar en la base de datos.
        - `python manage.py makemigrations`
        - `python manage.py migrate`
    - Crear usuario administrador: `python manage.py createsuperuser`
    - Para borrar toda la base de datos: `rm db.sqlite3`
- **Para cargar info por defecto**: `python manage.py cargar_datos`

## Mensajeria
Para crear una aplicación de mensajería donde los usuarios puedan comunicarse entre sí, vamos a dividirla en varias partes clave:

- **Modelo de Datos** (Base de Datos):
    - **Usuarios**: sistema de autenticación estándar de Django.
    - **Mensajes**: Crear un modelo para los mensajes, que estará vinculado a los usuarios.
    - **Conversaciones**: Se pueden tener conversaciones entre dos usuarios o grupos de usuarios.
- **Vistas y Rutas**:
    - **Lista de Conversaciones**: Los usuarios verán una lista de todas las conversaciones que han tenido.
    - **Vista de Mensajes**: Cada conversación tendrá una vista donde los usuarios pueden ver y enviar nuevos mensajes.

## Servidor
- Para activar el entorno virtual: 
    - `python -m venv .venv`
    - `.venv\Scripts\activate`
- Levanta el servidor: `python manage.py runserver`

## Instalaciones
- **Imágenes** para libros y avatares: `pip install Pillow`

## Test 
- para correr el test de blog: `python manage.py test libros`

### 1. **Pruebas de Modelos**

#### **Resena**
La clase `Resena` representa una reseña hecha por un usuario sobre un libro. En las pruebas, se valida lo siguiente:

- **Validación de la puntuación**: Se prueba que la puntuación de una reseña se mantenga dentro del rango válido (1 a 5 estrellas). Si se intenta guardar una reseña con una puntuación fuera de este rango, debe lanzarse una excepción `ValidationError`.

```python
def test_validar_puntuacion_invalida(self):
    resena = Resena(libro=self.libro, usuario=self.usuario, titulo="Test Review", contenido="Test Content", puntuacion=6)
    with self.assertRaises(ValidationError):
        resena.full_clean()  # Esto ejecuta la validación
```
### **Libro**
El modelo `Libro` tiene una relación con el modelo `AutorLibro` y se utiliza para almacenar información sobre los libros disponibles en la plataforma. Las pruebas incluyen la validación del cálculo del promedio de las puntuaciones de las reseñas de un libro.

#### **Promedio de Puntuación**
Se prueba que el promedio de las puntuaciones de todas las reseñas de un libro se calcule correctamente. Si no hay reseñas, el promedio debe ser `0`.

```python
def test_promedio_puntuacion(self):
    libro = Libro.objects.create(titulo="Test Book", descripcion="Test Description", fecha_publicacion="2022-01-01", autor_libro=self.autor)
    Resena.objects.create(libro=libro, usuario=self.usuario, titulo="Review 1", contenido="Good book", puntuacion=4)
    Resena.objects.create(libro=libro, usuario=self.usuario, titulo="Review 2", contenido="Nice read", puntuacion=5)
    self.assertEqual(libro.promedio_puntuacion(), 4)
```

#### Conversación y Mensajes

Los modelos `Conversacion` y `Mensaje` gestionan la interacción entre usuarios mediante conversaciones y mensajes. Se prueba lo siguiente:

- **Creación de conversación**: Se asegura que una conversación se cree correctamente con múltiples participantes.
- **Envío de mensaje**: Se verifica que un mensaje se pueda enviar correctamente dentro de una conversación y que los mensajes se ordenen por fecha de creación.


### 2. Pruebas de Funciones de Base de Datos

#### Relaciones entre Modelos

Se prueba que las relaciones entre los modelos `Libro`, `Resena`, `AutorLibro` y `Usuario` funcionen correctamente. Esto incluye:

- Verificar que las reseñas estén asociadas a un libro.
- Confirmar que un usuario pueda hacer reseñas de diferentes libros.

### 3. Pruebas de Integración

Además de las pruebas unitarias, se han implementado pruebas de integración para garantizar que los modelos interactúan correctamente en el flujo completo de datos. Esto abarca desde:

- La creación de un libro,
- Hasta la publicación de reseñas,
- Y el envío de mensajes en las conversaciones.

### 4. Estrategia de Pruebas

Las pruebas están basadas en el framework de pruebas de Django, utilizando `TestCase`. Cada prueba está diseñada para:

- **Asegurar que se cumplan las restricciones de los modelos** (por ejemplo, el rango de puntuación permitido en `Resena`).
- **Verificar la integridad de las relaciones entre modelos** (por ejemplo, que las reseñas estén correctamente asociadas con libros y usuarios).
- **Confirmar que las funciones de los modelos arrojen los resultados esperados** (como el cálculo del promedio de puntuación en los libros).

Cada operación sobre la base de datos es aislada para no afectar la integridad de otras pruebas.

## Borrar archivos / carpetas de github
- .venv
    - `git rm -r --cached .venv`
    - `git commit -m "Eliminando venv del índice de Git"`
    - `git add .gitignore`
    - `git commit -m "Actualizando .gitignore"`
- db.sqlite3
    - `git rm --cached db.sqlite3`
    - `git commit -m "Agregar db.sqlite3 al .gitignore`
- __pycache__
    - `git rm -r --cached libros/__pycache__ proyecto/__pycache__ libros/management/commands/__pycache__ libros/migrations/__pycache__`
    - `git commit -m "Eliminar __pycache__ del repositorio y agregarlo al .gitignore"`

## Requerimientos
- `pip freeze > requirements.txt`

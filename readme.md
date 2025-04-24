<h1 align="center">Mi blog de libros</h1>
<p align="center"><img src="myAvatar.png" width: "40%"></p>
<p align="center">by <b>Cecilia 💛 Perdomo</b></p>


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

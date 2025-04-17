<h1 align="center">Mi blog de libros</h1>
<p align="center"><img src="myAvatar.png" style="width: 50%"></p>
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

## Servidor
- Para activar el entorno virtual: 
    - `python -m venv .venv`
    - `.venv\Scripts\activate`
- Levanta el servidor: `python manage.py runserver`

## Instalaciones necesarias
- Imágenes para libros: `pip install Pillow`

## Test 
- para correr el test de blog: `python manage.py test blog`

## Borrar el .venv
- `git rm -r --cached .venv`
- `git commit -m "Eliminando venv del índice de Git"`
- `git add .gitignore`
- `git commit -m "Actualizando .gitignore"`
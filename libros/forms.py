from django import forms
from .models import Libro, AutorLibro, Resena, Avatar

# Par editar el formulario de usuario
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro	
        fields = ['titulo', 'descripcion', 'autor_libro', 'fecha_publicacion', 'portada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del libro'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del libro'}),
            'autor_libro': forms.Select(attrs={'class': 'form-select'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'portada': forms.ClearableFileInput(attrs={'class': "form-control", 'type': "file"}),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'autor_libro': 'Autor del libro',
            'fecha_publicacion': 'Fecha de publicación',
            'portada': 'Portada del libro',
        }
        error_messages = {
            'titulo': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El título no puede exceder los 200 caracteres.'
            },
            'descripcion': {
                'required': 'Este campo es obligatorio.'
            },
            'autor_libro': {
                'required': 'Este campo es obligatorio.'
            },
            'fecha_publicacion': {
                'required': 'Este campo es obligatorio.'
            },
            'portada': {
                'invalid': 'Formato de imagen no válido.',
                'invalid_image': 'La imagen no es válida.'
            }
        }

class AutorLibroForm(forms.ModelForm):
    class Meta:
        model = AutorLibro
        fields = ['nombre', 'biografia', 'fecha_nacimiento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del autor'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Biografía del autor'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'nombre': 'Nombre',
            'biografia': 'Biografía',
            'fecha_nacimiento': 'Fecha de nacimiento',
        }
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El nombre no puede exceder los 100 caracteres.'
            },
            'biografia': {
                'required': 'Este campo es obligatorio.'
            },
            'fecha_nacimiento': {
                'required': 'Este campo es obligatorio.'
            }
        }
       

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['libro', 'titulo', 'contenido', 'puntuacion']
        widgets = {
            'libro': forms.Select(attrs={'class': 'form-select'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la reseña'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido de la reseña'}),
            'puntuacion': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'libro': 'Libro',
            'titulo': 'Título',
            'contenido': 'Contenido',
            'puntuacion': 'Puntuación',
        }
        error_messages = {
            'libro': {
                'required': 'Este campo es obligatorio.'
            },
            'titulo': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El título no puede exceder los 100 caracteres.'
            },
            'contenido': {
                'required': 'Este campo es obligatorio.'
            },
            'puntuacion': {
                'required': 'Este campo es obligatorio.'
            }
        }
        
class EditUserForm(UserChangeForm):
    username = forms.CharField(
        required=True,
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    email = forms.EmailField(
        required=True,
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    first_name = forms.CharField(
        required=True,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        required=True,
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        }
        error_messages = {
            'username': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El nombre de usuario no puede exceder los 150 caracteres.'
            },
            'email': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un correo electrónico válido.'
            },
            'first_name': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El nombre no puede exceder los 30 caracteres.'
            },
            'last_name': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El apellido no puede exceder los 150 caracteres.'
            },
            'password': {
                'required': 'Este campo es obligatorio.'
            }
        }

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'}),
        }
        labels = {
            'imagen': 'Imagen de perfil',
        }
        error_messages = {
            'imagen': {
                'invalid': 'Formato de imagen no válido.',
                'invalid_image': 'La imagen no es válida.'
            }
        }
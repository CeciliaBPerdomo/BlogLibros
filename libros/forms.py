from django import forms
from .models import Libro, AutorLibro, Resena, Avatar, Perfil

# Par editar el formulario de usuario
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

###########################################################################################################################################
## Libros
###########################################################################################################################################
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

###########################################################################################################################################
## Autores
###########################################################################################################################################
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
       
###########################################################################################################################################
## Reseñas
###########################################################################################################################################
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

###########################################################################################################################################
## Usuarios
###########################################################################################################################################
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

    fecha_cumple = forms.DateField(
        required=False,
        label='Fecha de cumpleaños',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    biografia = forms.CharField(
        required=False,
        label='Biografía',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
    libro_favorito = forms.CharField(
        required=False,
        label='Libro favorito',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'fecha_cumple', 'biografia', 'libro_favorito']
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
    
    def save(self, commit=True):
        user = super().save(commit)
        perfil, creado = Perfil.objects.get_or_create(user=user)
        perfil.fecha_cumple = self.cleaned_data.get('fecha_cumple')
        perfil.biografia = self.cleaned_data.get('biografia')
        perfil.libro_favorito = self.cleaned_data.get('libro_favorito')
        if commit:
            perfil.save()
        return user

# Login de usuarios
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label='Usuario:',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    password = forms.CharField(
        required=True,
        label="Contraseña:",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}), 
    )
    class Meta:
        model = User
        fields = ['username', 'password']

# Registro de usuarios
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico',
    }))
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre'
    }))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Apellido'
    }))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña'
    }))
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repetir contraseña'
    }))
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre de usuario'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

###########################################################################################################################################
## Avatares
###########################################################################################################################################
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
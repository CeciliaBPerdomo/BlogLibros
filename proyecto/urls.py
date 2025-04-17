# proyecto/urls.py 
from django.contrib import admin
from django.urls import path, include
from libros import views

# Archivos de medios 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('libros/', include(('libros.urls', 'libros'), namespace='libros')),
]


# Servir archivos de medios durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
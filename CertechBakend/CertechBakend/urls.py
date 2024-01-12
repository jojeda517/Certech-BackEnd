"""
Configuración de URL para el proyecto CertechBakend.

La lista `urlpatterns` dirige las URL a las vistas. Para obtener más información, consulta:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

Ejemplos:

Vistas basadas en funciones
    1. Agrega una importación: from my_app import views
    2. Agrega una URL a urlpatterns: path('', views.home, name='home')

Vistas basadas en clases
    1. Agrega una importación: from other_app.views import Home
    2. Agrega una URL a urlpatterns: path('', Home.as_view(), name='home')

Inclusión de otro URLconf
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

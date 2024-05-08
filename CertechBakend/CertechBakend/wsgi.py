"""
Configuración WSGI para el proyecto CertechBakend.

Expone la aplicación WSGI como una variable a nivel de módulo llamada ``application``.

Para obtener más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CertechBakend.settings')

application = get_wsgi_application()

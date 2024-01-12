"""
Configuración ASGI para el proyecto CertechBakend.

Expone el objeto invocable ASGI como una variable a nivel de módulo llamada ``application``.

Para obtener más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CertechBakend.settings')

application = get_asgi_application()

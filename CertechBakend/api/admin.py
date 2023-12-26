from django.contrib import admin
from .models import Administrador, Firma, Participante

# Register your models here.

admin.site.register(Administrador)
admin.site.register(Firma)
admin.site.register(Participante)

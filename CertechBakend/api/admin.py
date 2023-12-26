from django.contrib import admin
from .models import Administrador, Firma, Participante, Evento

# Register your models here.

admin.site.register(Administrador)
admin.site.register(Firma)
admin.site.register(Participante)
admin.site.register(Evento)

from django.contrib import admin
from .models import Administrador, Firma, Participante, Evento, Certificado, DetalleCertificado,Plantilla

# Register your models here.

admin.site.register(Administrador)
admin.site.register(Firma)
admin.site.register(Participante)
admin.site.register(Evento)
admin.site.register(Certificado)
admin.site.register(DetalleCertificado)
admin.site.register(Plantilla)
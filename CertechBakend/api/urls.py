from django.urls import path
from .views import AdministradorView, FirmaView, FirmaUpdateView, ParticipanteView, ParticipanteFileView, EventoView, EventoUpdate,CertificadoView,CertificadoUpdateView,CertificadoDeleteView,DetalleCertificadoView,PlantillaCertificadoView

urlpatterns = [
    path('administrador/<str:usuario>/<str:clave>/',
         AdministradorView.as_view(), name='administrador_list'),
    path('firma/', FirmaView.as_view(), name='firma_list'),
    path('firma/<str:id_firma>/', FirmaView.as_view(), name='firma_proceso'),
    path('firmaupdate/<str:id_firma>/',
         FirmaUpdateView.as_view(), name='firma_update'),
    path('participante/', ParticipanteView.as_view(), name='participante_list'),
    path('participante/<str:id_participante>/',
         ParticipanteView.as_view(), name='participante_proceso'),
    path('participantefile/', ParticipanteFileView.as_view(),
         name='participante_list'),
    path('evento/', EventoView.as_view(), name='evento_list'),
    path('evento/<str:id_evento>/',
         EventoView.as_view(), name='evento_proceso'),
    path('eventoupdate/<str:id_evento>/',
         EventoUpdate.as_view(), name='evento_proceso'),
    path('certificado/', CertificadoView.as_view(), name='certificado_list'),
    path('certificado/<str:id_certificado>/', CertificadoView.as_view(), name='certificado_proceso'),
    
]

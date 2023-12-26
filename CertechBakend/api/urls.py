from django.urls import path
from .views import AdministradorView, FirmaView, FirmaUpdateView, ParticipanteView

urlpatterns = [
    path('administrador/<str:usuario>/<str:clave>/',
         AdministradorView.as_view(), name='administrador_list'),
    path('firma/', FirmaView.as_view(), name='firma_list'),
    path('firma/<str:id_firma>/', FirmaView.as_view(), name='firma_proceso'),
    path('firmaupdate/<str:id_firma>/',
         FirmaUpdateView.as_view(), name='firma_update'),
    path('participante/', ParticipanteView.as_view(), name='participante_list'),
    path('participante/<str:id_participante>/',
         ParticipanteView.as_view(), name='participante_proceso')
]

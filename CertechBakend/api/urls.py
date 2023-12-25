from django.urls import path
from .views import AdministradorView, FirmaView

urlpatterns = [
    path('administrador/<str:usuario>/<str:clave>/',
         AdministradorView.as_view(), name='administrador_list'),
    path('firma/', FirmaView.as_view(), name='firma_list'),
    path('firma/<str:id_firma>/', FirmaView.as_view(), name='firma_proceso')
]

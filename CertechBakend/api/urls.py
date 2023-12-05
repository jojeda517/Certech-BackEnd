from django.urls import path
from .views import AdministradorView

urlpatterns=[
    path('administrador/<str:usuario>/<str:clave>/', AdministradorView.as_view(), name='administrador_list')
]
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, FileResponse
from .constants import SUCCESS_MESSAGE, ERROR_MESSAGE, NOT_DATA_MESSAGE
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Administrador

# Create your views here.

class AdministradorView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, usuario=None, clave=None):
        if usuario or clave is not None:
            administradores = list(Administrador.objects.filter(
                usuario=usuario, clave=clave).values())
            if len(administradores) > 0:
                administrador = administradores[0]
                datos = {'administrador': administrador}
                return JsonResponse(datos)
            else:
                datos = NOT_DATA_MESSAGE
                return JsonResponse(datos, status=400)
        else:
            administradores = list(Administrador.objects.values())
            if len(administradores) > 0:
                datos = {'administradores': administradores}
                return JsonResponse(datos)
            else:
                return JsonResponse(datos, status=400)

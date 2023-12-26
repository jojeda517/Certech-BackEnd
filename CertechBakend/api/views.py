from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, FileResponse
from .constants import SUCCESS_MESSAGE, ERROR_MESSAGE, NOT_DATA_MESSAGE
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Administrador, Firma, Participante
from django.core.files.storage import default_storage
import os
import json

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


class FirmaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_firma=None):
        if (id_firma == None):
            firmas = list(Firma.objects.filter(estado_firma="Activo").values())
            if len(firmas) > 0:
                datos = {'firmas': firmas}
            else:
                datos = NOT_DATA_MESSAGE
        else:
            firma = Firma.objects.filter(id_firma=id_firma).values().first()
            if (firma != None):
                datos = {'firma': firma}
            else:
                datos = NOT_DATA_MESSAGE
        return JsonResponse(datos)

    def post(self, request):
        try:
            jsonData = request.POST
            imagen = request.FILES.get('firma')
            img_path = os.path.join('static', 'firmas', imagen.name)
            img_path = default_storage.save(img_path, imagen)
            with open(img_path, 'wb') as f:
                for chunk in imagen.chunks():
                    f.write(chunk)
            firma = Firma.objects.create(
                propietario_firma=jsonData['propietario_firma'],
                cargo_propietario=jsonData['cargo_propietario'],
                firma=img_path,
                estado_firma="Activo"
            )
            datos = Firma.objects.filter(
                id_firma=firma.id_firma).values().first()
            datos = {'firma': datos}
        except:
            return JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)

    def delete(self, request, id_firma=None):
        try:
            if (id_firma is not None and Firma.objects.filter(id_firma=id_firma, estado_firma='Activo').exists()):
                firma = Firma.objects.get(id_firma=id_firma)
                firma.estado_firma = 'Inactivo'
                firma.save()
                datos = SUCCESS_MESSAGE
            else:
                datos = NOT_DATA_MESSAGE
        except:
            return JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)


class FirmaUpdateView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id_firma=None):
        try:
            jsonData = request.POST
            imagen = request.FILES.get('firma')
            img_path = os.path.join('static', 'firmas', imagen.name)
            img_path = default_storage.save(img_path, imagen)
            with open(img_path, 'wb') as f:
                for chunk in imagen.chunks():
                    f.write(chunk)

            if (id_firma is not None and Firma.objects.filter(id_firma=id_firma, estado_firma='Activo').exists()):
                firma = Firma.objects.filter(id_firma=id_firma).get()
                firma.propietario_firma = jsonData['propietario_firma']
                firma.cargo_propietario = jsonData['cargo_propietario']
                firma.firma = img_path
                firma.save()
                datos = {'firma': Firma.objects.filter(
                    id_firma=id_firma).values().first()}
            else:
                datos = NOT_DATA_MESSAGE
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse(datos)


class ParticipanteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_participante=None):
        if (id_participante is None):
            participantes = list(Participante.objects.values())
            if (len(participantes) > 0):
                datos = {'participantes': participantes}
            else:
                datos = NOT_DATA_MESSAGE
        else:
            participante = Participante.objects.filter(
                id_participante=id_participante).values().first()
            if participante is not None:
                datos = {'participante': participante}
            else:
                datos = NOT_DATA_MESSAGE
        return JsonResponse(datos)

    def post(self, request):
        try:
            jsonData = json.loads(request.body)
            participante = Participante.objects.create(
                cedula=jsonData['cedula'],
                nombre_apellido=jsonData['nombre_apellido'],
                celular=jsonData['celular'],
                correo=jsonData['correo']
            )
            datos = Participante.objects.filter(
                id_participante=participante.id_participante).values().first()
        except:
            return JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)

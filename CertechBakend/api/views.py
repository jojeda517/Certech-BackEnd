from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, FileResponse
from .constants import SUCCESS_MESSAGE, ERROR_MESSAGE, NOT_DATA_MESSAGE
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Administrador, Firma, Participante, Evento
from django.core.files.storage import default_storage
import pandas as pd
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

    def put(self, request, id_participante):
        try:
            jsonData = json.loads(request.body)
            if Participante.objects.filter(id_participante=id_participante).exists():
                participante = Participante.objects.filter(
                    id_participante=id_participante).get()
                participante.cedula = jsonData['cedula']
                participante.nombre_apellido = jsonData['nombre_apellido']
                participante.celular = jsonData['celular']
                participante.correo = jsonData['correo']
                participante.save()
                datos = {'participante': Participante.objects.filter(
                    id_participante=id_participante).values().first()}
            else:
                datos = {'error': NOT_DATA_MESSAGE}
        except:
            datos = JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)

    def delete(self, request, id_participante):
        try:
            if Participante.objects.filter(id_participante=id_participante).exists():
                Participante.objects.filter(
                    id_participante=id_participante).delete()
                datos = SUCCESS_MESSAGE
            else:
                datos = NOT_DATA_MESSAGE
        except:
            datos = JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)


class ParticipanteFileView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            # Asegúrate de que el archivo Excel se haya enviado en la solicitud.
            if 'excel_file' in request.FILES:
                excel_file = request.FILES['excel_file']

                # Utiliza pandas para leer el archivo Excel.
                df = pd.read_excel(excel_file)

                # Itera sobre las filas del DataFrame y crea participantes.
                for _, row in df.iterrows():
                    participante = Participante.objects.create(
                        cedula=row['cedula'],
                        nombre_apellido=row['nombre_apellido'],
                        celular=row['celular'],
                        correo=row['correo']
                    )

                # Obtiene los datos del último participante creado.
                datos = Participante.objects.filter(
                    id_participante=participante.id_participante
                ).values().first()

                return JsonResponse(datos)

            else:
                return JsonResponse({"error": "No se proporcionó un archivo Excel"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class EventoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_evento=None):
        if id_evento is not None:
            evento = Evento.objects.filter(
                id_evento=id_evento).values().first()
            if evento is not None:
                datos = {'evento': evento}
            else:
                datos = NOT_DATA_MESSAGE
        else:
            eventos = list(Evento.objects.values())
            if len(eventos) > 0:
                datos = {'eventos': eventos}
            else:
                datos = NOT_DATA_MESSAGE
        return JsonResponse(datos)

    def post(self, request):
        try:
            jsonData = request.POST
            # Portada
            imagenPortada = request.FILES.get('portada')
            imgPort_path = os.path.join(
                'static', 'portada', imagenPortada.name)
            imgPort_path = default_storage.save(imgPort_path, imagenPortada)
            with open(imgPort_path, 'wb') as f:
                for chunk in imagenPortada.chunks():
                    f.write(chunk)
            # Logo
            imagenLogo = request.FILES.get('logo')
            imgLogo_path = os.path.join('static', 'logo', imagenLogo.name)
            imgLogo_path = default_storage.save(imgLogo_path, imagenLogo)
            with open(imgLogo_path, 'wb') as f:
                for chunk in imagenLogo.chunks():
                    f.write(chunk)

            evento = Evento.objects.create(
                nombre_evento=jsonData['nombre_evento'],
                tipo_evento=jsonData['tipo_evento'],
                descripcion_evento=jsonData['descripcion_evento'],
                portada=imgPort_path,
                logo=imgLogo_path
            )
            datos = Evento.objects.filter(
                id_evento=evento.id_evento).values().first()
            datos = {'evento': datos}
        except:
            return JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)

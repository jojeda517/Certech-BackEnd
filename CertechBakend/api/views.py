from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, FileResponse
from .constants import SUCCESS_MESSAGE, ERROR_MESSAGE, NOT_DATA_MESSAGE
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Administrador, Firma, Participante, Evento, Plantilla
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

                # Lista para almacenar todos los participantes
                participantes = []

                # Itera sobre las filas del DataFrame y crea participantes.
                for _, row in df.iterrows():
                    participante = Participante.objects.create(
                        cedula=row['cedula'],
                        nombre_apellido=row['nombre_apellido'],
                        celular=row['celular'],
                        correo=row['correo']
                    )
                    # Agrega el participante a la lista
                    participantes.append(participante)

                # Obtiene los datos de todos los participantes creados.
                datos = [{"id_participante": p.id_participante,
                          "cedula": p.cedula,
                          "nombre_apellido": p.nombre_apellido,
                          "celular": p.celular,
                          "correo": p.correo} for p in participantes]

                return JsonResponse(datos, safe=False)

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

    def delete(self, request, id_evento=None):
        try:
            if Evento.objects.filter(id_evento=id_evento).exists():
                Evento.objects.filter(
                    id_evento=id_evento).delete()
                datos = SUCCESS_MESSAGE
            else:
                datos = NOT_DATA_MESSAGE
        except:
            datos = JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)


class EventoUpdate(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id_evento):
        try:
            if Evento.objects.filter(id_evento=id_evento).exists():
                jsonData = request.POST
                # Portada
                imagenPortada = request.FILES.get('portada')
                imgPort_path = os.path.join(
                    'static', 'portada', imagenPortada.name)
                imgPort_path = default_storage.save(
                    imgPort_path, imagenPortada)
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
                evento = Evento.objects.filter(id_evento=id_evento).get()
                evento.nombre_evento = jsonData['nombre_evento']
                evento.tipo_evento = jsonData['tipo_evento']
                evento.descripcion_evento = jsonData['descripcion_evento']
                evento.portada = imgPort_path
                evento.logo = imgLogo_path
                evento.save()
                datos = Evento.objects.filter(
                    id_evento=evento.id_evento).values().first()
                datos = {'evento': datos}
            else:
                datos = NOT_DATA_MESSAGE
        except:
            return JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)


class PlantillaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_plantilla=None):
        try:
            if id_plantilla is None:
                # Si id_plantilla es None, retornar todos los datos de todas las plantillas
                plantillas = Plantilla.objects.all()
                datos = {'plantillas': list(plantillas.values())}
            else:
                # Si id_plantilla no es None, obtener los datos de una plantilla específica
                plantilla = Plantilla.objects.get(id_plantilla=id_plantilla)
                plantilla_path = plantilla.plantilla
                with open(plantilla_path, 'rb') as file:
                    response = HttpResponse(
                        file.read(), content_type='application/pdf')
                    return response
        except Plantilla.DoesNotExist:
            datos = ERROR_MESSAGE
        except Exception as e:
            datos = ERROR_MESSAGE

        return JsonResponse(datos)

    def post(self, request, id_plantilla=None):
        try:
            if Plantilla.objects.filter(id_plantilla=id_plantilla).exists():
                jsonData = request.POST
                plantillaDoc = request.FILES.get('plantilla')
                plantilla_path = os.path.join(
                    'static', 'plantilla', plantillaDoc.name)
                plantilla_path = default_storage.save(
                    plantilla_path, plantillaDoc)
                with open(plantilla_path, 'wb') as f:
                    for chunk in plantillaDoc.chunks():
                        f.write(chunk)
                plantilla = Plantilla.objects.filter(
                    id_plantilla=id_plantilla).get()
                plantilla.plantilla = plantilla_path
                plantilla.save()
                datos = Plantilla.objects.filter(
                    id_plantilla=plantilla.id_plantilla).values().first()
                datos = {'plantilla': datos}
            else:
                plantillaDoc = request.FILES.get('plantilla')
                plantilla_path = os.path.join(
                    'static', 'plantilla', plantillaDoc.name)
                plantilla_path = default_storage.save(
                    plantilla_path, plantillaDoc)
                with open(plantilla_path, 'wb') as f:
                    for chunk in plantillaDoc.chunks():
                        f.write(chunk)
                # Puedes ajustar esta parte según tus necesidades
                plantilla = Plantilla.objects.create(plantilla=plantilla_path)
                datos = {'plantilla': Plantilla.objects.filter(
                    id_plantilla=plantilla.id_plantilla).values().first()}
        except:
            return JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)

    def delete(self, request, id_plantilla):
        try:
            plantilla = Plantilla.objects.get(id_plantilla=id_plantilla)
            # Guarda la ruta del archivo antes de eliminar la plantilla
            plantilla_path = plantilla.plantilla
            plantilla.delete()  # Elimina la plantilla de la base de datos

            # Elimina el archivo físico asociado a la plantilla
            if os.path.exists(plantilla_path):
                os.remove(plantilla_path)

            datos = SUCCESS_MESSAGE
        except Plantilla.DoesNotExist:
            datos = NOT_DATA_MESSAGE
        except Exception as e:
            print(e)
            datos = ERROR_MESSAGE

        return JsonResponse(datos)

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, FileResponse
from .constants import SUCCESS_MESSAGE, ERROR_MESSAGE, NOT_DATA_MESSAGE
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Administrador, Firma, Participante, Evento, Plantilla, Certificado, Detalle_Certificado
from django.core.files.storage import default_storage
from django.core.files import File
import pandas as pd
import os
import json
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import *
from datetime import datetime
import locale

# Establecer el idioma local a español
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

# Create your views here.


class AdministradorView(View):
    """
    Vista para manejar operaciones relacionadas con administradores.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, usuario=None, clave=None):
        """
        Maneja las solicitudes GET para recuperar información sobre administradores.

        :param request: Objeto de solicitud Django.
        :param usuario: Nombre de usuario (opcional).
        :param clave: Clave (opcional).

        :return: JsonResponse con los datos del administrador o una respuesta de error.
        """
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
    """
    Vista para gestionar operaciones relacionadas con firmas en el sistema.

    Métodos admitidos:
        * GET: Obtiene detalles de las firmas. Puede obtener todas las firmas activas o una firma específica por su ID.
        * POST: Crea una nueva firma utilizando datos proporcionados en la solicitud.
        * DELETE: Desactiva (cambia el estado a 'Inactivo') una firma existente por su ID.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
        * SUCCESS_MESSAGE (dict): Mensaje de respuesta exitosa.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_firma=None):
        """
        Maneja las solicitudes GET para recuperar información sobre firmas.

        :param request: Objeto de solicitud Django.
        :param id_firma: Identificador único de la firma (opcional).

        :return: JsonResponse con detalles de las firmas o una respuesta de error.
        """
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
        """
        Maneja las solicitudes POST para crear una nueva firma.

        :param request: Objeto de solicitud Django.

        :return: JsonResponse con detalles de la nueva firma creada o una respuesta de error.
        """
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
        """
        Maneja las solicitudes DELETE para desactivar una firma existente.

        :param request: Objeto de solicitud Django.
        :param id_firma: Identificador único de la firma a desactivar (opcional).

        :return: JsonResponse indicando el resultado de la operación o una respuesta de error.
        """
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
    """
    Vista para gestionar la actualización de una firma existente en el sistema.

    Métodos admitidos:
        * POST: Actualiza los detalles de una firma existente utilizando datos proporcionados en la solicitud.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id_firma=None):
        """
        Maneja las solicitudes POST para actualizar una firma existente.

        :param request: Objeto de solicitud Django.
        :param id_firma: Identificador único de la firma a actualizar (opcional).

        :return: JsonResponse con detalles de la firma actualizada o una respuesta de error.
        """
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
    """
    Vista para gestionar operaciones relacionadas con participantes en el sistema.

    Métodos admitidos:
        * GET: Obtiene detalles de los participantes. Puede obtener todos los participantes o un participante específico por su ID.
        * POST: Crea un nuevo participante utilizando datos proporcionados en la solicitud.
        * PUT: Actualiza los detalles de un participante existente utilizando datos proporcionados en la solicitud.
        * DELETE: Elimina un participante existente por su ID.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
        * SUCCESS_MESSAGE (dict): Mensaje de respuesta exitosa.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_participante=None):
        """
        Maneja las solicitudes GET para recuperar información sobre participantes.

        :param request: Objeto de solicitud Django.
        :param id_participante: Identificador único del participante (opcional).

        :return: JsonResponse con detalles de los participantes o una respuesta de error.
        """
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
        """
        Maneja las solicitudes POST para crear un nuevo participante.

        :param request: Objeto de solicitud Django.

        :return: JsonResponse con detalles del nuevo participante creado o una respuesta de error.
        """
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
        """
        Maneja las solicitudes PUT para actualizar un participante existente.

        :param request: Objeto de solicitud Django.
        :param id_participante: Identificador único del participante a actualizar.

        :return: JsonResponse con detalles del participante actualizado o una respuesta de error.
        """
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
        """
        Maneja las solicitudes DELETE para eliminar un participante existente.

        :param request: Objeto de solicitud Django.
        :param id_participante: Identificador único del participante a eliminar.

        :return: JsonResponse indicando el resultado de la operación o una respuesta de error.
        """
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
    """
    Vista para manejar la carga de participantes desde un archivo Excel.

    Métodos admitidos:
        * POST: Procesa un archivo Excel enviado en la solicitud y crea participantes en base a los datos del archivo.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
        * SUCCESS_MESSAGE (dict): Mensaje de respuesta exitosa.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        """
        Maneja las solicitudes POST para procesar un archivo Excel y crear participantes.

        :param request: Objeto de solicitud Django.

        :return: JsonResponse con detalles de los participantes creados o una respuesta de error.
        """
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
    """
    Vista para manejar operaciones relacionadas con eventos.

    Métodos admitidos:
        * GET: Recupera información sobre eventos, ya sea un evento específico o todos los eventos disponibles.
        * POST: Crea un nuevo evento a partir de los datos proporcionados en la solicitud.
        * DELETE: Elimina un evento específico según el ID proporcionado.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
        * SUCCESS_MESSAGE (dict): Mensaje de respuesta exitosa.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_evento=None):
        """
        Maneja las solicitudes GET para recuperar información sobre eventos.

        :param request: Objeto de solicitud Django.
        :param id_evento: ID del evento (opcional).

        :return: JsonResponse con detalles del evento o una respuesta de error.
        """
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
        """
        Maneja las solicitudes POST para crear un nuevo evento.

        :param request: Objeto de solicitud Django.

        :return: JsonResponse con detalles del evento creado o una respuesta de error.
        """
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
        """
        Maneja las solicitudes DELETE para eliminar un evento.

        :param request: Objeto de solicitud Django.
        :param id_evento: ID del evento a eliminar.

        :return: JsonResponse con un mensaje de éxito o una respuesta de error.
        """
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
    """
    Vista para manejar la actualización de eventos.

    Métodos admitidos:
        * POST: Actualiza un evento existente según el ID proporcionado.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
        * SUCCESS_MESSAGE (dict): Mensaje de respuesta exitosa.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id_evento):
        """
        Maneja las solicitudes POST para actualizar un evento existente.

        :param request: Objeto de solicitud Django.
        :param id_evento: ID del evento a actualizar.

        :return: JsonResponse con detalles del evento actualizado o una respuesta de error.
        """
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
    """
    Vista para manejar operaciones relacionadas con plantillas.

    Métodos admitidos:
        * GET: Recupera información sobre plantillas o descarga una plantilla específica.
        * POST: Crea una nueva plantilla o actualiza una existente.
        * DELETE: Elimina una plantilla existente.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
        * SUCCESS_MESSAGE (dict): Mensaje de respuesta exitosa.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_plantilla=None):
        """
        Maneja las solicitudes GET para recuperar información sobre plantillas o descargar una plantilla específica.

        :param request: Objeto de solicitud Django.
        :param id_plantilla: ID de la plantilla a recuperar o descargar (opcional).

        :return: JsonResponse con detalles de la plantilla o una respuesta de error.
        """
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
        """
        Maneja las solicitudes POST para crear una nueva plantilla o actualizar una existente.

        :param request: Objeto de solicitud Django.
        :param id_plantilla: ID de la plantilla a actualizar (opcional).

        :return: JsonResponse con detalles de la plantilla creada o actualizada o una respuesta de error.
        """
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
        """
        Maneja las solicitudes DELETE para eliminar una plantilla existente.

        :param request: Objeto de solicitud Django.
        :param id_plantilla: ID de la plantilla a eliminar.

        :return: JsonResponse con mensaje de éxito o una respuesta de error.
        """
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


class CertificadoView(View):
    """
    Vista para manejar operaciones relacionadas con certificados.

    Métodos admitidos:
        * POST: Crea un nuevo certificado con las firmas proporcionadas y genera el certificado en formato PDF.

    Atributos:
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id_firma1, id_firma2):
        """
        Maneja las solicitudes POST para crear un nuevo certificado con las firmas proporcionadas y generar el certificado en formato PDF.

        :param request: Objeto de solicitud Django.
        :param id_firma1: ID de la primera firma asociada al certificado.
        :param id_firma2: ID de la segunda firma asociada al certificado.

        :return: JsonResponse con detalles del certificado creado o una respuesta de error.
        """
        try:
            jsonData = json.loads(request.body)
            certificado = Certificado.objects.create(
                id_administrador=jsonData['id_administrador'],
                id_participante=jsonData['id_participante'],
                id_evento=jsonData['id_evento'],
                id_plantilla=jsonData['id_plantilla']
            )

            # Obtén la plantilla asociada al certificado
            plantilla = Plantilla.objects.get(
                pk=jsonData['id_plantilla']).plantilla

            # Crea la instancia de Detalle_Certificado con las firmas correspondientes
            detalle_certificado1 = Detalle_Certificado.objects.create(
                id_certificado=certificado.id_certificado,
                id_firma=Firma.objects.get(pk=id_firma1).id_firma
            )

            detalle_certificado2 = Detalle_Certificado.objects.create(
                id_certificado=certificado.id_certificado,
                id_firma=Firma.objects.get(pk=id_firma2).id_firma
            )

            # Genera el certificado en PDF
            generar_certificado_pdf(
                certificado, plantilla, detalle_certificado1, detalle_certificado2)

            datos = Certificado.objects.filter(
                id_certificado=certificado.id_certificado).values().first()
        except Exception as e:
            print(e)
            return JsonResponse(ERROR_MESSAGE, status=400)
        return JsonResponse(datos)


class CertificadoValidoView(View):
    """
    Vista para verificar la validez de un certificado mediante su código único.

    Métodos admitidos:
        * GET: Obtiene detalles del certificado válido asociado al código único proporcionado.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no se encuentra el certificado.
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, codigo_unico):
        """
        Maneja las solicitudes GET para obtener detalles del certificado válido asociado al código único proporcionado.

        :param request: Objeto de solicitud Django.
        :param codigo_unico: Código único asociado al certificado.

        :return: JsonResponse con detalles del certificado válido o una respuesta de error.
        """
        try:
            if Certificado.objects.filter(codigo_unico=codigo_unico).exists():
                certificado = Certificado.objects.get(
                    codigo_unico=codigo_unico)
                administrador = Administrador.objects.get(
                    id_administrador=certificado.id_administrador).usuario
                evento = Evento.objects.get(
                    id_evento=certificado.id_evento).nombre_evento

                datos = {
                    'id_certificado': certificado.id_certificado,
                    'nombre_apellido': Participante.objects.get(id_participante=certificado.id_participante).nombre_apellido,
                    'administrador': administrador,
                    'evento': evento,
                    'fecha': certificado.fecha,
                    'codigo_unico': certificado.codigo_unico,
                    'url': certificado.url
                }
            else:
                datos = NOT_DATA_MESSAGE
        except Participante.DoesNotExist:
            datos = NOT_DATA_MESSAGE
        except Exception as e:
            return JsonResponse(ERROR_MESSAGE, status=400)

        return JsonResponse(datos)


class CertificadoParticipanteView(View):
    """
    Vista para obtener los certificados asociados a un participante mediante su número de cédula.

    Métodos admitidos:
        * GET: Obtiene la lista de certificados asociados al participante.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no se encuentra el participante o sus certificados.
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, cedula):
        """
        Maneja las solicitudes GET para obtener la lista de certificados asociados a un participante mediante su número de cédula.

        :param request: Objeto de solicitud Django.
        :param cedula: Número de cédula del participante.

        :return: JsonResponse con la lista de certificados asociados al participante o una respuesta de error.
        """
        try:
            participante = Participante.objects.get(cedula=cedula)
            certificados = Certificado.objects.filter(
                id_participante=participante.id_participante)
            datos = {'certificados': [{'id_certificado': certificado.id_certificado, 'nombre_apellido': participante.nombre_apellido, 'administrador': Administrador.objects.get(
                id_administrador=certificado.id_administrador).usuario, 'evento': Evento.objects.get(id_evento=certificado.id_evento).nombre_evento, 'fecha': certificado.fecha, 'codigo_unico': certificado.codigo_unico, 'url': certificado.url} for certificado in certificados]}
        except Participante.DoesNotExist:
            datos = NOT_DATA_MESSAGE
        except Exception as e:
            print(e)
            return JsonResponse(ERROR_MESSAGE, status=400)

        return JsonResponse(datos)


class ParticipantesEventoView(View):
    """
    Vista para obtener la lista de participantes asociados a un evento mediante su identificador.

    Métodos admitidos:
        * GET: Obtiene la lista de participantes asociados al evento.

    Atributos:
        * NOT_DATA_MESSAGE (dict): Mensaje de respuesta cuando no se encuentran certificados o participantes asociados al evento.
        * ERROR_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Despacha la solicitud, excluyendo la verificación CSRF.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_evento):
        """
        Maneja las solicitudes GET para obtener la lista de participantes asociados a un evento mediante su identificador.

        :param request: Objeto de solicitud Django.
        :param id_evento: Identificador del evento.

        :return: JsonResponse con la lista de participantes asociados al evento o una respuesta de error.
        """
        try:
            certificados = Certificado.objects.filter(id_evento=id_evento)
            participantes_info = {}

            for certificado in certificados:
                participante_id = certificado.id_participante

                # Verificar si ya hemos procesado este participante
                if participante_id not in participantes_info:
                    participante = Participante.objects.get(
                        id_participante=participante_id)
                    participantes_info[participante_id] = {
                        'id_participante': participante.id_participante,
                        'cedula': participante.cedula,
                        'nombre_apellido': participante.nombre_apellido,
                        'celular': participante.celular,
                        'correo': participante.correo
                    }

            datos = {'participantes': list(participantes_info.values())}
        except Certificado.DoesNotExist:
            datos = NOT_DATA_MESSAGE
        except Participante.DoesNotExist:
            datos = NOT_DATA_MESSAGE
        except Exception as e:
            return JsonResponse(ERROR_MESSAGE, status=400)

        return JsonResponse(datos)


def generar_certificado_pdf(certificado, plantilla_path, detalle_certificado1, detalle_certificado2):
    """
    Genera un certificado en formato PDF combinando la información del certificado, la plantilla,
    y las firmas proporcionadas.

    :param certificado: Objeto Certificado que contiene la información necesaria para generar el certificado.
    :param plantilla_path: Ruta del archivo PDF de la plantilla del certificado.
    :param detalle_certificado1: Objeto Detalle_Certificado que contiene la información de la primera firma.
    :param detalle_certificado2: Objeto Detalle_Certificado que contiene la información de la segunda firma.
    """

    participante = Participante.objects.filter(
        id_participante=certificado.id_participante).values().first()
    firma1 = Firma.objects.filter(
        id_firma=detalle_certificado1.id_firma).values().first()
    firma2 = Firma.objects.filter(
        id_firma=detalle_certificado2.id_firma).values().first()
    evento = Evento.objects.filter(
        id_evento=certificado.id_evento).values().first()
    print(firma1['firma'])
    print(firma2['firma'])
    print(participante)
    # Abrir el archivo de la plantilla PDF existente
    with open(plantilla_path, 'rb') as plantilla_file:
        pdf_reader = PdfReader(plantilla_file)

        # Crear un nuevo PDF en memoria
        buffer = BytesIO()
        pdf_writer = PdfWriter()

        firma1_path = firma1['firma']
        firma2_path = firma2['firma']

        # Iterar sobre las páginas de la plantilla
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]

            # Crear un nuevo lienzo para agregar contenido
            packet = BytesIO()
            # Dimensiones en milímetros
            ancho_mm = 297
            alto_mm = 210

            # Convertir a pulgadas (1 pulgada = 25.4 mm)
            ancho_pulgadas = ancho_mm / 25.4
            alto_pulgadas = alto_mm / 25.4

            # Convertir a puntos (1 pulgada = 72 puntos)
            ancho_puntos = ancho_pulgadas * 72
            alto_puntos = alto_pulgadas * 72

            # Tamaño de página para ReportLab
            tamano_pagina = (ancho_puntos, alto_puntos)

            # Usar el tamaño de página en ReportLab
            can = canvas.Canvas(packet, pagesize=tamano_pagina)
            ancho_documento, alto_documento = can._pagesize
            print(ancho_documento)
            print(alto_documento)

            # Agregar texto al lienzo, puedes personalizar esto según tus necesidades

            # Confiere el presente
            can.setFont("Helvetica", 30)
            longitud_texto_enc = can.stringWidth(
                f"Confiere el presente", "Helvetica", 30)
            can.drawString((ancho_puntos/2)-(longitud_texto_enc/2),
                           (alto_puntos-(alto_puntos/4))-20, f"Confiere el presente")

            # CERTIFICADO
            can.setFont("Helvetica", 30)
            longitud_texto_cert = can.stringWidth(
                f"CERTIFICADO A:", "Helvetica", 30)
            can.drawString((ancho_puntos/2)-(longitud_texto_cert/2),
                           (alto_puntos-(alto_puntos/4)-50), f"CERTIFICADO A:")

            # Participante
            can.setFont("Times-Roman", 50)
            longitud_texto = can.stringWidth(
                f"{participante['nombre_apellido']}".upper(), "Times-Roman", 50)
            can.drawString((ancho_puntos - longitud_texto) / 2, (alto_puntos/2) +
                           15, f"{participante['nombre_apellido']}".upper())

            # Confiere el presente
            can.setFont("Helvetica", 14)
            longitud_texto_con = can.stringWidth(
                f"Por haber participado y aprobado el curso:", "Helvetica", 14)
            can.drawString((ancho_puntos/2)-(longitud_texto_con/2), (alto_puntos -
                           (alto_puntos/2))-15, f"Por haber participado y aprobado el curso:")

            # Evento
            can.setFont("Times-Roman", 30)
            longitud_texto_evento = can.stringWidth(
                f"{evento['nombre_evento']}".upper(), "Times-Roman", 30)
            can.drawString((ancho_puntos/2)-(longitud_texto_evento/2),
                           (alto_puntos-(alto_puntos/2))-50, f"{evento['nombre_evento']}".upper())

            # Fecha
            fecha_formateada = certificado.fecha.strftime("%d de %B de %Y")
            print(fecha_formateada)
            can.setFont("Helvetica", 14)
            longitud_texto_fecha = can.stringWidth(
                "Ambato, "+fecha_formateada, "Helvetica", 14)
            can.drawString(ancho_puntos-longitud_texto_fecha-50,
                           (alto_puntos-(alto_puntos/2))-70, "Ambato, "+fecha_formateada)

            # codigo
            can.setFont("Helvetica", 10)
            can.drawString(1, 1, f"{certificado.codigo_unico}")

            # Agregar imagen de la firma 1 al lienzo
            can.drawImage(firma1_path, (ancho_puntos/4)-100, 100, 200, 100)

            # Agregar imagen de la firma 2 al lienzo
            can.drawImage(firma2_path, ancho_puntos -
                          (ancho_puntos/4)-100, 100, 200, 100)

            # tamaño texto firma 1
            can.setFont("Helvetica", 20)
            longitud_texto_firma1 = can.stringWidth(
                f"{firma1['propietario_firma']}", "Helvetica", 20)
            longitud_texto_firma2 = can.stringWidth(
                f"{firma2['propietario_firma']}", "Helvetica", 20)
            # agregar a quien pertenece la firma
            can.drawString((ancho_puntos/4)-longitud_texto_firma1 /
                           2, 75, f"{firma1['propietario_firma']}")

            # agregar a quien pertenece la firma
            can.drawString((ancho_puntos - (ancho_puntos/4) -
                           longitud_texto_firma2/2), 75, f"{firma2['propietario_firma']}")

            # tamaño texto cargo
            can.setFont("Helvetica", 25)
            longitud_texto_cargo_firma1 = can.stringWidth(
                f"{firma1['cargo_propietario']}", "Helvetica", 25)
            longitud_texto_cargo_firma2 = can.stringWidth(
                f"{firma2['cargo_propietario']}", "Helvetica", 25)
            # agregar a quien pertenece la firma
            can.drawString((ancho_puntos/4)-longitud_texto_cargo_firma1 /
                           2, 50, f"{firma1['cargo_propietario']}")

            # agregar a quien pertenece la firma
            can.drawString((ancho_puntos - (ancho_puntos/4) -
                           longitud_texto_cargo_firma2/2), 50, f"{firma2['cargo_propietario']}")

            # Cerrar el lienzo
            can.save()
            packet.seek(0)
            can.showPage()

            # Combina el lienzo generado con la página de la plantilla
            overlay = PdfReader(packet)
            page.merge_page(overlay.pages[0])

            # Añadir la página modificada al nuevo PDF
            pdf_writer.add_page(page)

        # Directorio para guardar el certificado
        certificado_directory = f'static/certificado/'
        certificado_path = f'{certificado_directory}{certificado.codigo_unico}.pdf'

        # Crear el directorio si no existe
        if not os.path.exists(certificado_directory):
            os.makedirs(certificado_directory)

        # Guardar el nuevo PDF en la ubicación deseada
        with open(certificado_path, 'wb') as certificado_file:
            pdf_writer.write(certificado_file)

    # Actualizar el campo pdf_path en el modelo Certificado
    certificado.url = certificado_path
    certificado.save()

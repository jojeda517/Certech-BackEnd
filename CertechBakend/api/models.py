from django.db import models
import uuid


class Administrador(models.Model):
    """
    Modelo para representar un administrador en el sistema.

    Atributos:
        * id_administrador (AutoField): Identificador único del administrador (clave primaria).
        * usuario (CharField): Nombre de usuario del administrador.
        * clave (CharField): Contraseña del administrador.
        * cedula (CharField): Número de cédula del administrador.
        * correo (CharField): Dirección de correo electrónico del administrador.
        * celular (CharField): Número de teléfono celular del administrador.

    Meta:
        * managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
        * db_table (str): Nombre de la tabla en la base de datos ('administradores' en este caso).

    Ejemplo de uso:

        admin = Administrador(
        usuario='nombre_usuario',
        clave='contraseña_segura',
        cedula='1234567890',
        correo='admin@example.com',
        celular='1234567890'
        )

        admin.save()
    """

    id_administrador = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    celular = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'administradores'


class Firma(models.Model):
    """
    Modelo para representar una firma en el sistema.

    Atributos:
        * id_firma (AutoField): Identificador único de la firma (clave primaria).
        * propietario_firma (CharField): Nombre del propietario de la firma.
        * cargo_propietario (CharField): Cargo del propietario de la firma.
        * firma (CharField): Representación de la firma (puede ser una ruta de archivo, URL o datos de imagen, dependiendo de la implementación).
        * estado_firma (CharField): Estado actual de la firma (por ejemplo, activa, inactiva, pendiente).

    Meta:
        * managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
        * db_table (str): Nombre de la tabla en la base de datos ('firmas' en este caso).

    Ejemplo de uso:

        firma = Firma(
        propietario_firma='Nombre Propietario',
        cargo_propietario='Cargo del Propietario',
        firma='ruta_o_datos_de_firma',
        estado_firma='Activa'
        )

        firma.save()
    """

    id_firma = models.AutoField(primary_key=True)
    propietario_firma = models.CharField(max_length=100)
    cargo_propietario = models.CharField(max_length=100)
    firma = models.CharField(max_length=255)
    estado_firma = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'firmas'


class Participante(models.Model):
    """
    Modelo para representar a un participante en el sistema.

    Atributos:
        * id_participante (AutoField): Identificador único del participante (clave primaria).
        * cedula (CharField): Número de cédula del participante.
        * nombre_apellido (CharField): Nombre y apellido del participante.
        * celular (CharField): Número de teléfono celular del participante.
        * correo (CharField): Dirección de correo electrónico del participante.

    Meta:
        * managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
        * db_table (str): Nombre de la tabla en la base de datos ('participantes' en este caso).

    Ejemplo de uso:

        participante = Participante(
        cedula='1234567890',
        nombre_apellido='Nombre Apellido',
        celular='1234567890',
        correo='participante@example.com'
        )

        participante.save()
    """

    id_participante = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    nombre_apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'participantes'


class Evento(models.Model):
    """
    Modelo para representar un evento en el sistema.

    Atributos:
        * id_evento (AutoField): Identificador único del evento (clave primaria).
        * nombre_evento (CharField): Nombre del evento.
        * tipo_evento (CharField): Tipo o categoría del evento.
        * descripcion_evento (TextField): Descripción detallada del evento.
        * portada (CharField): Ruta o enlace a la imagen de portada del evento.
        * logo (CharField): Ruta o enlace al logo del evento.
        * fecha_creacion (DateTimeField): Fecha y hora de creación del evento (se actualiza automáticamente al crear el evento).

    Meta:
        * managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
        * db_table (str): Nombre de la tabla en la base de datos ('eventos' en este caso).

    Ejemplo de uso:

        evento = Evento(
        nombre_evento='Nombre del Evento',
        tipo_evento='Tipo de Evento',
        descripcion_evento='Descripción detallada del evento.',
        portada='ruta_o_enlace_a_la_imagen_de_portada',
        logo='ruta_o_enlace_al_logo',
        )

        evento.save()
    """

    id_evento = models.AutoField(primary_key=True)
    nombre_evento = models.CharField(max_length=255)
    tipo_evento = models.CharField(max_length=100)
    descripcion_evento = models.TextField()
    portada = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'eventos'


class Plantilla(models.Model):
    """
    Modelo para representar una plantilla en el sistema.

    Atributos:
        * id_plantilla (AutoField): Identificador único de la plantilla (clave primaria).
        * plantilla (CharField): Ruta o enlace a la plantilla.

    Meta:
        * managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
        * db_table (str): Nombre de la tabla en la base de datos ('plantillas' en este caso).

    Ejemplo de uso:

        plantilla = Plantilla(
        plantilla='ruta_o_enlace_a_la_plantilla',
        )
        plantilla.save()
    """

    id_plantilla = models.AutoField(primary_key=True)
    plantilla = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'plantillas'


class Certificado(models.Model):
    """
    Modelo para representar un certificado en el sistema.

    Atributos:
        * id_certificado (AutoField): Identificador único del certificado (clave primaria).
        * id_administrador (IntegerField): Identificador del administrador asociado al certificado.
        * id_participante (IntegerField): Identificador del participante asociado al certificado.
        * id_evento (IntegerField): Identificador del evento asociado al certificado.
        * id_plantilla (IntegerField): Identificador de la plantilla asociada al certificado.
        * fecha (DateTimeField): Fecha y hora de creación del certificado (se actualiza automáticamente al crear el certificado).
        * url (CharField): Ruta o enlace al certificado.
        * codigo_unico (UUIDField): Código único asociado al certificado (generado automáticamente).

    Meta:
        * managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
        * db_table (str): Nombre de la tabla en la base de datos ('certificados' en este caso).

    Ejemplo de uso:

        certificado = Certificado(
        id_administrador=1,
        id_participante=2,
        id_evento=3,
        id_plantilla=4,
        url='ruta_o_enlace_al_certificado',
        )

        certificado.save()
    """

    id_certificado = models.AutoField(primary_key=True)
    id_administrador = models.IntegerField()
    id_participante = models.IntegerField()
    id_evento = models.IntegerField()
    id_plantilla = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=255)
    codigo_unico = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        managed = False
        db_table = 'certificados'


class Detalle_Certificado(models.Model):
    """
    Modelo para representar los detalles asociados a un certificado en el sistema.

    Atributos:
        * id_detalle (AutoField): Identificador único del detalle (clave primaria).
        * id_certificado (IntegerField): Identificador del certificado asociado al detalle.
        * id_firma (IntegerField): Identificador de la firma asociada al detalle.

    Meta:
        * managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
        * db_table (str): Nombre de la tabla en la base de datos ('detalle_certificados' en este caso).
    """

    id_detalle = models.AutoField(primary_key=True)
    id_certificado = models.IntegerField()
    id_firma = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_certificados'

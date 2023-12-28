from django.db import models


class Administrador(models.Model):
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
    id_firma = models.AutoField(primary_key=True)
    propietario_firma = models.CharField(max_length=100)
    cargo_propietario = models.CharField(max_length=100)
    firma = models.CharField(max_length=255)
    estado_firma = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'firmas'


class Participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    nombre_apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'participantes'


class Evento(models.Model):
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

class Certificado(models.Model):
    id_certificado = models.AutoField(primary_key=True)
    id_administrador = models.IntegerField()
    id_participante = models.IntegerField()
    id_evento = models.IntegerField()
    id_plantilla = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    codigo_unico = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'certificados'


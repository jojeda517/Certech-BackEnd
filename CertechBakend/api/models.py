from django.db import models

class Administrador(models.Model):
    id_administrador=models.AutoField(primary_key=True)
    usuario=models.CharField(max_length=50)
    clave=models.CharField(max_length=50)
    cedula=models.CharField(max_length=10)
    correo=models.CharField(max_length=50)
    celular=models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'administradores'

class Firma(models.Model):
    id_firma=models.AutoField(primary_key=True)
    propietario_firma=models.CharField(max_length=100)
    cargo_propietario=models.CharField(max_length=100)
    firma=models.CharField(max_length=255)
    estado_firma=models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'firmas'
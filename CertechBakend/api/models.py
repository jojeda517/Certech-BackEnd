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

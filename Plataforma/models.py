from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    nombre=models.CharField(max_length=20,verbose_name="nombre")
    apellidos=models.CharField(max_length=20,verbose_name="apellidos")
    usuario=models.CharField(max_length=15,verbose_name="usuario")
    contraseña=models.CharField(max_length=20,verbose_name="contraseña")

    def admin(self):
        return "{}, {}".format(self.apellidos,self.nombre)

    def __str__(self):
        return self.admin()

class Publicacion(models.Model):

    contenido=models.CharField(max_length=150,verbose_name="contenido")
    user=models.CharField(max_length=15,verbose_name="usuario")

class Venta(models.Model):

    precio_t=models.FloatField()
    user=models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def admin(self):
        return "X{} {}".format(self.precio_t,self.user)

    def __str__(self):
        return self.admin()


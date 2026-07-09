from django.db import models

class Docente(models.Model):
    TIPOS_SANGRE = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    cedula = models.CharField(max_length=10, unique=True)
    tipo_sangre = models.CharField(max_length=3, choices=TIPOS_SANGRE)
    direccion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='docentes/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

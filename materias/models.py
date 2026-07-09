from django.db import models
from docentes.models import Docente

class Curso(models.Model):
    JORNADAS = [
        ('Matutina', 'Matutina'),
        ('Vespertina', 'Vespertina'),
        ('Nocturna', 'Nocturna'),
    ]
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()
    nivel = models.CharField(max_length=50)
    horas = models.IntegerField()
    jornada = models.CharField(max_length=20, choices=JORNADAS)
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre

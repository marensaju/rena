from django.db import models
from django.utils import timezone

class Agendar(models.Model):
    usuario = models.ForeignKey('auth.User')
    actividad = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado =models.BooleanField(default=True)
    fecha_actividad = models.DateTimeField(blank=True, null=True)

    def crearactividad(self):
        self.fecha_actividad = timezone.now()
        self.save()

    def __str__(self):
        return self.actividad

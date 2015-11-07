from django.shortcuts import render
from django.utils import timezone
from .models import Agendar
def listar_publicaciones(request):
    actividades = Agendar.objects.filter(fecha_actividad__lte=timezone.now()).order_by('fecha_actividad')
    return render(request, 'agenda/listar_publicaciones.html', {'actividades': actividades})


# Create your views here.

from django.shortcuts import render
from django.utils import timezone
from .models import Agendar
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm

def listar_publicaciones(request):
    actividades = Agendar.objects.filter(fecha_actividad__lte=timezone.now()).order_by('fecha_actividad')
    return render(request, 'agenda/listar_publicaciones.html', {'actividades': actividades})
def actividad_detalle(request, pk):
    actividades = get_object_or_404(Agendar, pk=pk)
    return render(request, 'agenda/actividad_detalle.html', {'actividades': actividades})
def actividad_nueva(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect('agenda.views.actividad_detalle', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'agenda/editar_actividad.html', {'form': form})

def actividad_editar(request, pk):
    post = get_object_or_404(Agendar, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect('agenda.views.actividad_detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'agenda/editar_actividad.html', {'form': form})
# Create your views here.

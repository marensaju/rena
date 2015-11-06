from django.shortcuts import render
def listar_publicaciones(request):
    return render (request, 'agenda/listar_publicaciones.html',{})

# Create your views here.

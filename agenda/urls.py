from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.listar_publicaciones),
    url(r'^post/(?P<pk>[0-9]+)/$', views.actividad_detalle),
    url(r'^post/new/$', views.actividad_nueva, name='actividad_nueva'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.actividad_editar, name='actividad_editar'),

]

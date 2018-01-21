from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views

app_name = 'mr'

urlpatterns = [
    url(r'^$', login, {'template_name':'base/login.html'}, name='login'),
    url(r'^alumnos/add$', views.AlumnoCreateView.as_view(), name='alumno_add'),
    url(r'^alumnos/list', views.AlumnoList.as_view(),name='alumno_list'),
    url(r'^usuarios/add', views.UsuarioCreateView.as_view(), name='usuarios_add'),
    url(r'^usuarios/list', views.UsuarioList.as_view(),name='usuarios_list'),
    url(r'^index$', views.IndexView.as_view(), name='index'),
    url(r'^ajax/get_time$', views.get_servidor_time, name='hora_servidor')
]


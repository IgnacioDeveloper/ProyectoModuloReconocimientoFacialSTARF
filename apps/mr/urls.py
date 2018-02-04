from django.conf.urls import url, include
from django.contrib.auth.views import login, logout_then_login
from . import views

app_name = 'mr'

urlpatterns = [
    url(r'^login$', login, {'template_name':'base/login.html'}, name='login'),
    url(r'^logout$', logout_then_login, name='logout'),
    url(r'^index$', views.IndexView.as_view(), name='index'),
    url(r'^ajax/get_time$', views.get_servidor_time, name='hora_servidor'),
    url(r'^alumnos/list', views.AlumnoList.as_view(),name='alumnos_list'),
    url(r'^alumnos/add$', views.AlumnoCreateView.as_view(), name='alumnos_add'),
    url(r'^alumnos/modify/(?P<pk>\d+)$', views.AlumnoUpdateView.as_view(), name='alumnos_modify'),
    url(r'^alumnos/eliminate/(?P<pk>\d+)$', views.AlumnoDeleteView.as_view(), name='alumnos_eliminate'),
    url(r'^usuarios/list', views.UsuarioList.as_view(),name='usuarios_list'),
    url(r'^usuarios/add', views.UsuarioCreateView.as_view(), name='usuarios_add'),
    url(r'^usuarios/modify/(?P<pk>\d+)$', views.UsuarioUpdateView.as_view(), name='alumnos_modify'),
    url(r'^usuarios/eliminate/(?P<pk>\d+)$', views.UsuarioDeleteView.as_view(), name='alumnos_eliminate'),
]


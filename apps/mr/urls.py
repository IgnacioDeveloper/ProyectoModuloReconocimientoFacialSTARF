from django.conf.urls import url, include
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'mr'

urlpatterns = [
    url(r'^login$', login, {'template_name':'base/login.html'}, name='login'),
    url(r'^logout$', logout_then_login, name='logout'),
    url(r'^index$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^ajax/get_time$',views.get_servidor_time, name='hora_servidor'),
    url(r'^alumnos/list', login_required(views.AlumnoList.as_view()),name='alumnos_list'),
    url(r'^alumnos/add$', login_required(views.AlumnoCreateView.as_view()), name='alumnos_add'),
    url(r'^alumnos/modify/(?P<pk>\d+)$', login_required(views.AlumnoUpdateView.as_view()), name='alumnos_modify'),
    url(r'^alumnos/eliminate/(?P<pk>\d+)$', login_required(views.AlumnoDeleteView.as_view()), name='alumnos_eliminate'),
    url(r'^aulas/list', login_required(views.AulaList.as_view()),name='aulas_list'),
    url(r'^aulas/add$', login_required(views.AulaCreateView.as_view()), name='aulas_add'),
    url(r'^aulas/modify/(?P<pk>\d+)$', login_required(views.AulaUpdateView.as_view()), name='aulas_modify'),
    url(r'^aulas/eliminate/(?P<pk>\d+)$', login_required(views.AulaDeleteView.as_view()), name='aulas_eliminate'),
    url(r'^usuarios/list', login_required(views.UsuarioList.as_view()),name='usuarios_list'),
    url(r'^usuarios/add', login_required(views.UsuarioCreateView.as_view()), name='usuarios_add'),
    url(r'^usuarios/modify/(?P<pk>\d+)$', login_required(views.UsuarioUpdateView.as_view()), name='alumnos_modify'),
    url(r'^usuarios/eliminate/(?P<pk>\d+)$', login_required(views.UsuarioDeleteView.as_view()), name='alumnos_eliminate'),
]


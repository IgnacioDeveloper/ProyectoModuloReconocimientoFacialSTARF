from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponse
from apps.mr.models import Alumno, Usuario
from apps.mr.forms import UsuarioForm, AlumnoForm
from servertasks.clock import Reloj
import json

"""VIEWS"""

class IndexView(generic.TemplateView):
    template_name = "../templates/mr/index.html"

class AlumnoList(generic.ListView):
    model = Alumno
    template_name = "../templates/mr/list_templates/alumno_list.html"

class AlumnoCreateView(generic.CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = "../templates/mr/crud_forms/create_alumno.html"

    def get_success_url(self):
        return reverse_lazy("mr:"+self.request.POST.get('oldURLdata').replace('/', '_'))

class UsuarioList(generic.ListView):
    model = Usuario
    template_name = "../templates/mr/list_templates/usuario_list.html"

class UsuarioCreateView(generic.CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "../templates/mr/crud_forms/create_usuario.html"

    def get_success_url(self):
        return reverse_lazy("mr:"+self.request.POST.get('oldURLdata').replace('/', '_'))

"""REQUESTS"""

def get_servidor_time(request):
    return HttpResponse(Reloj.get_servidor_time())












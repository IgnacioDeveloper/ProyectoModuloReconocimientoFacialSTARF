from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from apps.mr.models import Alumno
from apps.mr.forms import AlumnoForm, UsuarioForm
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
    template_name = "../templates/mr/forms_templates/alumno_form.html"

    def get_success_url(self):
        return reverse_lazy("mr:"+self.request.POST.get('oldURLdata').replace('/', '_'))


class AlumnoUpdateView(generic.UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = "../templates/mr/forms_templates/alumno_form.html"
    success_url = reverse_lazy("mr:alumnos_list")

class AlumnoDeleteView(generic.DeleteView):
    model = Alumno
    form_class = AlumnoForm
    template_name = "../templates/mr/messages_templates/message.html"
    success_url = reverse_lazy("mr:alumnos_list")

class UsuarioList(generic.ListView):
    model = User
    template_name = "../templates/mr/list_templates/usuario_list.html"

class UsuarioCreateView(generic.CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "../templates/mr/forms_templates/usuario_form.html"

    def get_success_url(self):
        return reverse_lazy("mr:"+self.request.POST.get('oldURLdata').replace('/', '_'))

class UsuarioUpdateView(generic.UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = "../templates/mr/forms_templates/usuario_form.html"
    success_url = reverse_lazy("mr:usuarios_list")

class UsuarioDeleteView(generic.DeleteView):
    model = User
    form_class = UsuarioForm
    template_name = "../templates/mr/forms_templates/usuario_form.html"
    success_url = reverse_lazy("mr:usuarios_list")

"""REQUESTS"""

def get_servidor_time(request):
    return HttpResponse(Reloj.get_servidor_time())












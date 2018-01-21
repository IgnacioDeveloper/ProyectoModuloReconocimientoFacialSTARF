from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'mr/', include('apps.mr.urls')),
    url(r'^admin/', admin.site.urls)
]

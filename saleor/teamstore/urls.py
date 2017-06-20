from django.conf.urls import url, include

from . import views as teamstore_views



urlpatterns = [
    url(r'^login/$', teamstore_views.login, name='login'),
]

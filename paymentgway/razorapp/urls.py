from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^razor/$', views.index),
        url(r'^razor/purchase/$', views.success),
        url(r'^razor/login/$', views.login),
        url(r'razor/logged/$', views.logged_in),
]

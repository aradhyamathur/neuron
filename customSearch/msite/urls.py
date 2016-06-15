from django.conf.urls import url
from . import views
from . import api
urlpatterns = [
    url(r'^student/create/$', views.create_form),
    url(r'^student/home/$', views.home),
    url(r'^student/search/$', views.search),
    url(r'^student/list/$', api.StudentList.as_view())
]

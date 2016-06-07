from django.conf.urls import url
# from .api import PersonDetailView, PersonList, PersonCreate
from . import api
urlpatterns = [
    url(r'^search/$', api.PersonList.as_view()),
    url(r'^search/user/create/$', api.PersonCreate.as_view()),
    url(r'^search/(?P<name>[a-zA-Z]+)/$', api.PersonDetailView.as_view()),

]

from django.conf.urls import url
from .import views

appname = 'lobbys'

urlpatterns = [
    url(r'^(?P<lobbyid>[\w-]{,50})/$', views.lobby, name='lobby'),
]

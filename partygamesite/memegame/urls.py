from django.conf.urls import url
from . import views

app_name = 'memegame'

urlpatterns = [
    url(r'^$', views.Home.as_view(), name="start"),
]

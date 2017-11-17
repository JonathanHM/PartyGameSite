from django.conf.urls import url
from django.contrib.auth import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
]

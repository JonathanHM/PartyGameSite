from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# memegame views.py

#######################################################################
#                       Class based views                             #
#######################################################################
class Home(LoginRequiredMixin, TemplateView):
    template_name = "memegame/home.html"


#######################################################################
#                       Function based views                          #
#######################################################################

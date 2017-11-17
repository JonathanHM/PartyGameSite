from django.shortcuts import render
from django.views.generic import TemplateView

# memegame views.py

#######################################################################
#                       Class based views                             #
#######################################################################
class Home(TemplateView):
    template_name = "memegame/home.html"


#######################################################################
#                       Function based views                          #
#######################################################################

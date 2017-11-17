from django.shortcuts import render
from django.views.generic import TemplateView

# songgame views.py

#######################################################################
#                       Class based views                             #
#######################################################################
class Home(TemplateView):
    template_name = "songgame/home.html"


#######################################################################
#                       Function based views                          #
#######################################################################

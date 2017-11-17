from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# songgame views.py

#######################################################################
#                       Class based views                             #
#######################################################################
class Home(LoginRequiredMixin, TemplateView):
    template_name = "songgame/home.html"


#######################################################################
#                       Function based views                          #
#######################################################################

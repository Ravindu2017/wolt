from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Restaurants


class AboutView(TemplateView):
    template_name = "menu/list.html"

    def get(self, request):
        ##Fetch objects from database and send it to
        ##HTML page as argument

        ##Example was a testing model that only used
        ##parameters, name, description, and online
        #places = Example.objects.all()

        ##All objects of Restaurant model are called
        places = Restaurants.objects.all()

        args = {'restaurants': places}

        return render(request, self.template_name, args)

class AlphabetView(TemplateView):
    template_name = "menu/Normal.html"

    def get(self, request):

        ##Django's inbuilt order_by function sorts database column values
        places_ordered = Restaurants.objects.all().order_by("name")
        args = {'restaurants': places_ordered}
        return render(request, self.template_name, args)

class ZalphabetView(TemplateView):
    ##Extra view for viewing the restaurants from reverse order
    template_name = "menu/Reversed.html"

    def get(self, request):

        ##Adding a dash helps to reverse the order
        places_reversed = Restaurants.objects.all().order_by("-name")
        args = {'restaurants': places_reversed}
        return render(request, self.template_name, args)

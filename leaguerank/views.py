from django.shortcuts import render

# Create your views here.

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Leaguerank

class leaguerankBaseView(View):
    model = Leaguerank
    fields = '__all__'
    success_url = reverse_lazy('leaguerank:all')

class leaguerankListView(leaguerankBaseView, ListView):
    """View to list all leagueranks.
    Use the 'leaguerank_list' variable in the template
    to access all leaguerank objects"""

class leaguerankDetailView(leaguerankBaseView, DetailView):
    """View to list the details from one leaguerank.
    Use the 'leaguerank' variable in the template to access
    the specific leaguerank here and in the Views below"""

class leaguerankCreateView(leaguerankBaseView, CreateView):
    """View to create a new leaguerank"""

class leaguerankUpdateView(leaguerankBaseView, UpdateView):
    """View to update a leaguerank"""

class leaguerankDeleteView(leaguerankBaseView, DeleteView):
    """View to delete a leaguerank"""

from django.forms.models import model_to_dict
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from .models import Item
# Create your views here.

class WishList(ListView):
    model = Item

class WishItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'
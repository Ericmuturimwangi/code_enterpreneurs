from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializations import ItemSerializer
from django.http import HttpResponse


# Create your views here.

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def home_view(request):
    return HttpResponse("My first django API")
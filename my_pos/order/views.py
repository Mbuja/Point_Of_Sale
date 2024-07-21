from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action 
from .models import Person
from .serializers import PersonSerializer
# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    #The endpiont to allow users to be views

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


def index(request):
    return HttpResponse("<h1>This is the orders page </h1>")


def orders_list(request):
    orders = [
        {'id':1,'product': 'Product Milk '},
        {'id':2,'product': 'Product Eggs'},
        {'id':3,'product': 'Product Coffee '},
    ]
    context = {
        'orders':orders,
    }
    return JsonResponse(context)
    #return render(request,'order.html',context)
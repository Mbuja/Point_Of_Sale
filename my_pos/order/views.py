from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

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
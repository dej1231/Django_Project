from django.shortcuts import render

from .models import Product

# Create your views here.

def home_view(request, id):
    obj = Product.objects.get(id=id)
    context ={
        "object": obj
    }
    return render(request, "home.html", context)
# def home_view(request):
#     obj = Product.objects.all
#     context ={
#         "object": obj
#     }
#     return render(request, "home.html", context)
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Product

# Create your views here.

def home_view(request):
    query_set = Product.objects.all()
    context ={
        "object": query_set 
    }
    return render(request, "home.html", context)

def product_edit(request, id):
    obj = Product.objects.get(id=id)
    context ={
        "object": obj
    }
    return render(request, "product_edit.html", context)

def product_delete(request, id):
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('/')
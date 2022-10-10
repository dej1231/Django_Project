from django.shortcuts import render, redirect
from .forms import ProductForm

from .models import Product

# Create your views here.

def product_view(request):
    query_set = Product.objects.all()
    context ={
        "object": query_set 
    }
    return render(request, "home.html", context)

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product_create.html", context)

def product_update(request, id=id):
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product_update.html", context)

def product_delete(request, id):
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('/')
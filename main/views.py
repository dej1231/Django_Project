from django.shortcuts import render, redirect

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

# def delete_product(request, id):
#     obj = Product.objects.get(id=id)
#     if request.method == "POST":
#         obj.delete()
#         return redirect('../')
#     context ={
#         "object": obj
#     }
#     return render(request, "products/product_delete.html", context)
from django.shortcuts import render, redirect
from .forms import ProductForm

from .models import Product

# Create your views here.

def product_view(request):
    query_set = Product.objects.all().values()
    context ={
        "object": query_set 
    }
    # print(query_set)
    # print(type(context))
    return render(request, "product_view.html", context)

def product_create(request):
    name = request.POST['name']
    desc = request.POST['desc']
    qty = request.POST['qty']
    price = request.POST['price']
    if 'is_avbl' in request.POST:
        is_avbl = True
    else:
        is_avbl = False
    product = Product(name = name, description = desc, quantity = qty, price = price,is_available = is_avbl)
    product.save()
    return redirect('/')
    # form = ProductForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = ProductForm()
    #     return redirect('/')
    # context = {
    #     'form': form
    # }
    # return render(request, "product_create.html", context)

def product_update(request, id):
    name = request.POST['name']
    desc = request.POST['desc']
    qty = request.POST['qty']
    price = request.POST['price']
    # is_avbl = request.POST.get['is_avbl',False]
    if 'is_avbl' in request.POST:
        is_avbl = True
    else:
        is_avbl = False
    product = Product.objects.get(id=id)
    product.name = name
    product.description = desc
    product.quantity = qty
    product.price = price
    product.is_available = is_avbl
    product.save()
    return redirect('/')
    # obj = Product.objects.get(id=id)
    # form = ProductForm(request.POST or None, instance=obj)
    # print(obj)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    # context = {
    #     'form': form
    # }
    # return render(request, "product_update.html", context)

def product_delete(request,id):
    print(id)
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('/')

def product_get(request,id):
    obj = Product.objects.get(id=id)
    ctx = {
        'data': obj
    }
    print(id)
    return id

def product_mockup(request):
    # query_set = Product.objects.all().values()
    # context ={
    #     "object": query_set 
    # }
    # print(query_set)
    # print(type(context))
    return render(request, "product_mock.html")

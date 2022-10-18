from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm
import datetime
# Create your views here.

def staff_view(request):
    # query_set = Staff.objects.all().values()
    query_set = Staff.objects.get(id=1)
    context ={
        "object": query_set 
    }
    now = datetime.datetime.now()
    print(now)
    return render(request, "staff/staff_view.html", context)

def staff_create(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StaffForm()
        return redirect('/')
    context = {
        'form': form
    }
    
    return render(request, "staff/staff_create.html", context)

# def product_update(request, id=id):
#     obj = Staff.objects.get(id=id)
#     form = StaffForm(request.POST or None, instance=obj)
#     print(obj)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     context = {
#         'form': form
#     }
#     return render(request, "product_update.html", context)

# def staff_delete(id):
#     obj = Staff.objects.get(id=id)
#     obj.delete()
#     return redirect('/')
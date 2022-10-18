
from django.urls import path
from .views import (
    product_view,
    product_create,
    product_update,
    product_delete,
    )

urlpatterns = [
    path('', product_view),
    path('view/', product_view),
    path('create/', product_create),
    path('update/<int:id>/', product_update), 
    path('delete/<int:id>/', product_delete),
]

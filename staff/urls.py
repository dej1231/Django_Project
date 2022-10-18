
from django.urls import path
from .views import (
    staff_view,
    staff_create,
    )
urlpatterns = [
    path('', staff_view),
    path('create/', staff_create),
]

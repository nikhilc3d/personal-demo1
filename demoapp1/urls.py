from django.urls import path
from . import views

urlpatterns = [
    path('funct/',views.fun_name),
    path('',views.fun_name)
]
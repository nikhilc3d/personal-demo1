from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def fun_name(request):
    #return HttpResponse('Hello World')
    return render(request,'index.html',{"name": "Nikhil"})
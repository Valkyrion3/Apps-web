from .models import *
from .forms import *
from django.shortcuts import render, redirect 

def mostrar(request):
    panes= pan.objects.all()
    context={
        'panes':panes,
    }
    return render (request,'mostrar.html',context)

# Create your views here.
def landing(request):
    a= pan.objects.all()
    #t = 3
    #b= pan.objects.filter(t)
    context={
        'pan':a,
    }
    return render (request,'mostrar.html',context)


def post_agregar(request):
    if request.method == "POST":
        form = panecito(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("formato valido")
            
        return redirect('landing')

def calc (request):
    return render (request, 'calculadora.html')

def convertidor(request):
    return render(request,"convert.html")

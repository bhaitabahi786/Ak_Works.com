from django.shortcuts import render
from django.http import HttpResponse

def quotation(request):
    return render(request,"quotation.html")

def painting(request):
    return HttpResponse("this is painting")


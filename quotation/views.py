from django.shortcuts import render
from django.http import HttpResponse

def quotation(request):
    return HttpResponse("this is quotation page")


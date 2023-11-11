from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')
def munnu(request):
    return HttpResponse('<h1><marquee>hello macha</h1></marquee>')

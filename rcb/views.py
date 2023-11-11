from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')
def junnu(request):
    return HttpResponse('<h1><marquee>Hi, junnu ma yala unnavu. All good</h1></marquee>')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')
def raisa(request):
    return HttpResponse('<h1><marquee>hello raisa, how are you raisa</h1></marquee>')


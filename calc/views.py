from django.shortcuts import render
from django.shortcuts import HttpResponse
from urllib.request import urlopen
# Create your views here.
def calc(request):
    return render(request, 'index.html')
    return HttpResponse ("Helllo Guys")
    
    

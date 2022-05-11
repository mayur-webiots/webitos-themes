from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def testing(request):
    return render(request,'myapp/testing.html')

def index(request):
    return render(request,'myapp/index.html')
    # return HttpResponse('hello')
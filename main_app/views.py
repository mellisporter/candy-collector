from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#define the home view
def home(request):
    return HttpResponse('Hello world, this is the candy app!')

def about(request):
    return render(request, 'about.html')
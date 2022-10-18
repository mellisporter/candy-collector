from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# import 
from main_app.models import Candy

# MODELS

# class Candy:
#     def __init__(self, name, house, description):
#         self.name= name
#         self.house= house
#         self.description = description

# candy = [
#     Candy('Twizzlers' , 'The Porters' , 'Red and chewy'),
#     Candy('Reeses', 'The Millers' , 'The best there is.')
# ]

#define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def candy_index(request):
    candy = Candy.objects.all()
    return render(request, 'candy/index.html' , {'candy' : candy})

def candy_detail(request, candy_id):
  candy = Candy.objects.get(id=candy_id)
  return render(request, 'candy/detail.html', { 'candy': candy })



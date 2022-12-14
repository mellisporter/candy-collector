from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

# import 
from main_app.models import Candy

from .forms import IngredientsForm

from main_app.models import Brand

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.detail import DetailView



# MODELS
class CandyCreate(CreateView):
    model= Candy
    fields = '__all__'
    success_url = '/candy/'

class CandyUpdate(UpdateView):
    model= Candy
    fields = '__all__'

class CandyDelete(DeleteView):
    model = Candy
    success_url='/candy/'

class BrandCreate(CreateView):
    model = Brand
    fields = '__all__'
    success_url= '/brand'

class BrandUpdate(UpdateView):
    model= Brand
    fields = '__all__'

class BrandDelete(DeleteView):
    model = Brand
    success_url='/brand/'

class BrandDetail(DetailView):
    model = Brand
    template_name = 'brand/detail.html'



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

def brand_index(request):
    brand = Brand.objects.all()
    return render(request, 'brand/index.html', {'brand': brand})

def candy_detail(request, candy_id):
  candy = Candy.objects.get(id=candy_id)
  # get brands not assigned
  brands_candy_doesnt_have= Brand.objects.exclude(id__in = candy.brand.all().values_list('id'))
  # calling the ingredients form 
  ingredients_form = IngredientsForm()
  return render(request, 'candy/detail.html', { 'candy': candy , 'ingredients_form': 
  ingredients_form , 'brands': brands_candy_doesnt_have})


def add_ingredients(request, candy_id):
    # creates the ModelForm using data
    form = IngredientsForm(request.POST)
    if form.is_valid():
        new_ingredients = form.save(commit=False)
        new_ingredients.candy_id = candy_id
        new_ingredients.save()
    return redirect('detail' , candy_id=candy_id)


def assoc_brand(request, candy_id, brand_id):
    Candy.objects.get(id=candy_id).brand.add(brand_id)
    return redirect('detail', candy_id=candy_id)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/' , views.about, name= 'about'),
    path('candy/', views.candy_index, name='index'),
    path('candy/<int:candy_id>/', views.candy_detail, name='detail'),
    # new route used to show a form and create a candy
    path('candy/create/', views.CandyCreate.as_view(), name='candy_create'),
]


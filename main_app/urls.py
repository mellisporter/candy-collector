from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/' , views.about, name= 'about'),
    path('candy/', views.candy_index, name='index'),
    path('candy/<int:candy_id>/', views.candy_detail, name='detail'),
    # new route used to show a form and create a candy
    path('candy/create/', views.CandyCreate.as_view(), name='candy_create'),
    path('candy/<int:pk>/update/', views.CandyUpdate.as_view(), name='candy_update'),
    path('candy/<int:pk>/delete/', views.CandyDelete.as_view(), name="candy_delete"),
    path('candy/<int:candy_id>/add_ingredients/' , views.add_ingredients, name='add_ingredients'),
    path('brand/create/', views.BrandCreate.as_view(), name='brand_create'),
    path('brand/' , views.brand_index, name='index'),
    path('brand/<int:pk>/update/', views.BrandUpdate.as_view(), name='brand_update'),
    path('brand/<int:pk>/delete', views.BrandDelete.as_view(), name='brand_delete'),
    path('brand/<int:pk>/', views.BrandDetail.as_view(), name='brand_detail'),

]


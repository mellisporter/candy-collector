from django.contrib import admin

from main_app.models import Candy

# import second model
from main_app.models import Ingredients

# Register your models here.
admin.site.register(Candy)
# adding new ingredient model to admin
admin.site.register(Ingredients)
from django.contrib import admin
from .models import *
# Register your models here.


class BurgerMenu(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    
    
admin.site.register(DrinkMenu)
admin.site.register(SetMenu)
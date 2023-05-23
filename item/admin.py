from django.contrib import admin
from .models import Category, Item
# Register your models here.
# tell Django that we want the database to appear in the admin board
admin.site.register(Category)
admin.site.register(Item)

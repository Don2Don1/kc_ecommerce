from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=["id","name","slug","img","description","date_added"]
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=["id","category","title","slug","price","description","img","quantity","max_quantity","min_quantity","date_added"]
admin.site.register(Product, ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=["id","full_name","email","subject","message","date_added"]
admin.site.register(Contact, ContactAdmin)
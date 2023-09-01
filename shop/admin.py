from django.contrib import admin
from parler.admin import TranslatableAdmin
from . import models

@admin.register(models.Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

@admin.register(models.Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['id','name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

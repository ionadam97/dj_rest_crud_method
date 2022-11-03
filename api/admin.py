from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ adding product class to the admin site """

    list_display = ('title', 'description', 'created')
    search_fields = ('title',)
    # list_editable = []
    list_filter =  ['title',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ adding category class to the admin site """

    list_display = ('name', 'description')
    search_fields = ('name',)
    # list_editable = []
    list_filter =  ['name',]
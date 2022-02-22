from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'size', 'price')
    summernote_fields = ('content')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'description', 'price', 'image')
    search_field = ('name')


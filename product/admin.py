from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ['name', 'description']
    ordering = ('name',)
    summernote_fields = ('description',)


# @admin.register(Id)
# class IdAdmin(admin.ModelAdmin):
#     list_display = ('name',)



from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='product')
    path('details/', get_product_details, name='details'),
    path('add/', product_add, name='add'),
]

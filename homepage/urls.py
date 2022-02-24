from . import views
from django.urls import path

urlpatterns = [
    path('homepage', views.PostList.as_view(), name='homepage'),
]

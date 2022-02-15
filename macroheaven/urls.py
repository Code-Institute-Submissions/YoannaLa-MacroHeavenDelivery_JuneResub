"""macroheaven URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menulist.views import get_menu_list
from homepage.views import get_home_page 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('macroblog.urls'), name='macroblog_urls'),
    path('summernote/', include('django_summernote.urls')),
    path('', get_menu_list, name='get_menu_list'),
     path('homepage/', get_home_page, name='homepage'),
]

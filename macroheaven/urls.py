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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', get_home_page, name='homepage'),
    path('admin/', admin.site.urls),
    path('macroblog/', include('macroblog.urls'), name='macroblog_urls'),
    path('menu/', get_menu_list, name='menulist'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

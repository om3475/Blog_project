"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from blogapp import urls
import blogapp
import blogapp.urls
from . import views
from blogapp import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('category/', include('blogapp.urls')),
    path('search/',blog_views.search_blog,name='search'),
    path('registration/',blog_views.registration,name='registration'),
    path('login/',blog_views.user_login,name='login'),
    path('logout/',blog_views.user_logout,name='logout'),
    path('blogs/<slug:slug>/',blog_views.single_blog,name='single_blog'),

    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

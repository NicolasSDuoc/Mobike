"""mobike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app.views import delete_user, home, list_user, login_user, modify_user, register,logout,list_user_id,geolocator,bicycle
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login_user,name='login'),
    path('logout',logout,name='logout'),
    path('list-user/',list_user,name='list-user'),
    path('modify-user/<id>/',modify_user,name='modify-user'),
    path('delete-user/<id>/',delete_user,name='delete-user'),
    path('list-user-id',list_user_id,name='list-user-id'),
    path('geolocator',geolocator,name='geolocator'),
    path('bicycle/<id>/',bicycle,name='bicycle'),
]

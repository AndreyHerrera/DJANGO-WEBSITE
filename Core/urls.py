"""Core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from LandingPage import views as LandingPage_views
from Password import views as Password_views
from ToDoList import views as ToDoList_views


urlpatterns = [
    path('admin_login/', admin.site.urls),
    path('', LandingPage_views.home, name = 'Home'),
    path('password/', Password_views.password_generator, name = 'Password'),
    path('to-do-list/', ToDoList_views.todolist, name = 'ToDoList'),
    path('to-do-list/create', ToDoList_views.createtodolist, name = 'CreateToDoList'),
    path('to-do-list/delete/<id>', ToDoList_views.deletetodolist, name = 'DeleteToDoList'),
]

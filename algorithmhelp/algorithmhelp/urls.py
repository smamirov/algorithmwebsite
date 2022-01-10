"""algorithmhelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path
from projectApp.views import home_page
from addAlgo.views import addAlgo, displayAlgo, viewAlgo, changeAlgo, deleteAlgo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home.html'),
    path('addalgo/', addAlgo, name="addalgo.html"),
    path('viewalgo/', viewAlgo, name="viewalgo.html"),
    path('viewalgo/displayalgo/<int:id>', displayAlgo, name="displayalgo.html"),
    path('viewalgo/changealgo/<int:id>', changeAlgo, name="changealgo.html"),
    path('viewalgo/deletealgo/<int:id>', deleteAlgo, name="deletealgo.html"),
]

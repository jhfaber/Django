"""ModelsTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from ModelTemplatesApp import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    #SHOW THE USERS
    url(r'^users/', views.users),
    #SAVE NEW USERS
    url(r'^users2/', views.users2),
    #GO INSIDE OF THE ADMIN DJANGO PAGE
    url(r'^admin/', admin.site.urls),
    #DON'T DO IT NOTHING
    url(r'^help/', views.help, name= 'help'),
    #SHOW AN BASIC FORM WITH PROTECTION OF BOTS.
    url(r'^formpage/', views.form_name_view, name= 'form_name'),

#We cand add more urls from ModelTamplatesApp, we can use two URLs
#http://127.0.0.1:8000/ModelTemplatesApp/ for call the index function of the
#other file

    url(r'ModelTemplatesApp/',include('ModelTemplatesApp.urls'))

]

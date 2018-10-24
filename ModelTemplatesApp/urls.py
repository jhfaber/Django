from django.conf.urls import url
from ModelTemplatesApp import views


#TEMPLATE TAGGING IT IS SO IMPORTANT!!!! FOR RELATIVE URLS, IT IS THE NAME OF THIS URLS!

app_name = 'template'

urlpatterns = [
    url(r'^$',views.template, name='template'),
    url(r'^relative/', views.relative, name= 'relative'),
    url(r'^other/', views.other, name= 'other'),
]

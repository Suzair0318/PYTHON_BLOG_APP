from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('BlogComment' , views.blogComment , name='blogComment'),
    path('' , views.blogHome , name='bloghome' ),    
    path('<str:name>' , views.blogPost , name='blogPost'),
   
]

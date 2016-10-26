'''
Created on 26 oct. 2016

@author: leo
'''
from django.conf.urls import  url
import views 

urlpatterns = [
    url(r'^$', views.room, name='home'),
]
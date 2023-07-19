from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("capture_image",capture_image,name="capture_image"),

]
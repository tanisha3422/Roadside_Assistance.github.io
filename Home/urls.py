from django.contrib import admin
from django.urls import path, include;
from Home import views;

urlpatterns = [
    path('', views.index, name="Home"),
    path('About',views.About, name="About"),
    path('FAQ',views.FAQ, name="FAQ"),
]
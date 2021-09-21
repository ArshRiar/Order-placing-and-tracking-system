"""Urls of Customer app"""

from django.contrib import admin
from django.urls import path
from Customers import views
urlpatterns = [
    path('', views.home),
    path('products',views.product_range),
    path('login', views.loginuser),
    path('register', views.register),   
    path('<int:pid>', views.Product_desc),
    path('login/<int:pid>', views.Product_desc),
    path('logout', views.logoutuser),
    path('login/', views.LoggedProducts),
    path('login/LoggedProducts', views.LoggedProducts),
    path('LoggedProducts', views.LoggedProducts),
    path('login/logout', views.logoutuser),
    path('login/dashboard', views.dashboard),
    path('dashboard', views.dashboard),
    path('login/profile', views.profile), 
    path('login/products/<int:pid>', views.Product_desc),
    path('summary', views.summary),
    path('trackorder', views.tracker),
    path('login/trackorder', views.tracker),
    path('profile', views.profile),
]


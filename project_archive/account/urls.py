from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.signup, name="register"),
    path('', views.signin, name='login'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logout, name='logout'),
]

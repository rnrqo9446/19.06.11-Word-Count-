from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('result/', views.result, name = 'result')
]
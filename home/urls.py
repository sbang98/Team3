from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'
urlpatterns = [
    path('intro/', views.intro, name='intro'),
    path('', views.index, name='index'),
]

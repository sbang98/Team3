from django.urls import path
from . import views

app_name = 'result'
urlpatterns = [
    path('', views.result_list, name="result_list"),
    path('show1/', views.show_1, name="show1"),
    path('show2/', views.show_2, name="show2"),
    path('show3/', views.show_3, name="show3"),
    path('show4/', views.show_4, name="show4"),
    path('show5/', views.show_5, name="show5"),
]
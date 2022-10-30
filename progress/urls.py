from django.urls import path
from . import views

app_name = 'progress'
urlpatterns = [
    path('', views.progress_list, name="progress_list"),
    path('step1/', views.step_1, name="step1"),
    path('step2/', views.step_2, name="step2"),
    path('step3/', views.step_3, name="step3"),
    path('step4/', views.step_4, name="step4"),
    path('step5/', views.step_5, name="step5"),
]
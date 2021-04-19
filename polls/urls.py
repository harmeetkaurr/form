from django.urls import path
from . import views


urlpatterns = [
    path('college/', views.college_form, name='college_form'),
    path('school/', views.school_form, name='school_form'),
    path('login/', views.login, name='login'),
]
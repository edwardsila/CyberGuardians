from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('training/<int:module_id>/', views.training, name='training'),
    path('training/', views.training_list, name='training_list'),
    path('submit_quiz/<int:quiz_id>/', views.submit_quiz, name='submit_quiz'),
]

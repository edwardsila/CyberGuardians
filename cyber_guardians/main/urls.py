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
    path('quiz/<int:quiz_id>/', views.quiz_view, name='quiz'),
    path('report/', views.report_incident, name='report_incident'),
    path('success/', views.report_success, name='report_success'),
    path('list/', views.report_list, name='report_list')
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.end_user_login, name='login'),
    path('signup/', views.end_user_signup, name='register'),
    path('bms/admin/', views.admin_login)
]
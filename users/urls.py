from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.end_user_login),
    path('signup/', views.end_user_signup),
    path('admin/', views.admin_login)
]
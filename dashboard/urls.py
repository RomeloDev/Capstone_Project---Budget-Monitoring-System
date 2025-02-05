from django.urls import path
from . import views

urlpatterns = [
    path('end_user/home/', views.end_user_home, name="dashboard"),
    path('end_user/purchase-request/', views.purchase_request),
    path('end_user/view-budget/', views.view_budget),
    path('end_user/settings/', views.end_user_settings),
    path('admin/dashboard/', views.admin_home),
    path('admin/client-accounts/', views.admin_client_accounts),
    path('admin/admin-accounts/', views.admin_accounts_page),
    path('admin/budget-allocation/', views.admin_budget_allocation),
    path('admin/dept-requests/', views.admin_department_request)
]
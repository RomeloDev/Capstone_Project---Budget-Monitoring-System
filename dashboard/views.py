from django.shortcuts import render

# Create your views here.
def end_user_home(request):
    return render(request, 'dashboard/end_user/home.html')

def purchase_request(request):
    return render(request, 'dashboard/end_user/purchase_request.html')

def view_budget(request):
    return render(request, 'dashboard/end_user/view_budget.html')

def end_user_settings(request):
    return render(request, 'dashboard/end_user/settings.html')

def admin_home(request):
    return render(request, 'dashboard/admin/home.html')

def admin_client_accounts(request):
    return render(request, 'dashboard/admin/client_accounts.html')

def admin_accounts_page(request):
    return render(request, 'dashboard/admin/admin_accounts.html')

def admin_budget_allocation(request):
    return render(request, 'dashboard/admin/budget_allocation.html')

def admin_department_request(request):
    return render(request, 'dashboard/admin/department_request.html')
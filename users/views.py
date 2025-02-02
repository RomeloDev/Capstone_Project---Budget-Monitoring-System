from django.shortcuts import render

# Create your views here.
def end_user_login(request):
    return render(request, 'users/end_user_login.html', {"form_class": "login-form"})

def end_user_signup(request):
    return render(request, 'users/end_user_signup.html', {'form_class' : 'signup-form'})

def admin_login(request):
    return render(request, 'users/admin_login.html', {'cssClass' : 'login-form'})
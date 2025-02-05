from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User

# Create your views here.
def end_user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user_obj = User.objects.get(username=username)
            print(f"User exists: {user_obj.username}, Hashed Password: {user_obj.password}")
        except User.DoesNotExist:
            print("User does not exist!")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/end_user_login.html', {"error": "Invalid Credentials!"})
    
    return render(request, 'users/end_user_login.html', {"form_class": "login-form"})

def end_user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        department = request.POST['department']
        confirm_password = request.POST['confirm-password']
        
        if password != confirm_password:
            return render(request, 'users/end_user_signup.html', {"error": "Password and Confirm Password are must equal."})
        
        user = User.objects.create_user(username=username, email=email, password=password, department=department)
        
        # Debugging: Print the hashed password
        print(f"User Created: {user.username}, Hashed Password: {user.password}")
        
        return redirect('login')
        
    return render(request, 'users/end_user_signup.html', {'form_class': 'signup-form'})

def admin_login(request):
    return render(request, 'users/admin_login.html', {'cssClass' : 'login-form'})
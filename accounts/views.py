from django.shortcuts import render, redirect
from .firebase_config import auth
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            request.session['uid'] = str(user['idToken'])
            return redirect('dashboard')
        except:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            messages.success(request, "Account created successfully")
            return redirect('login')
        except:
            messages.error(request, "Error creating account")
            return redirect('register')
    return render(request, "register.html")

def dashboard_view(request):
    if 'uid' not in request.session:
        return redirect('login')
    return render(request, "dashboard.html")

def logout_view(request):
    if request.method == 'POST':
        try:
            del request.session['uid']
        except KeyError:
            pass
        messages.success(request, "Logged out successfully.")
        return redirect('login')
    else:
        return redirect('dashboard')  # Don't allow GET for logout

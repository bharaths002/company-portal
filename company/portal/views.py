from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import re

# ✅ Check Username Availability (AJAX)
def check_username(request):
    username = request.GET.get('username', '').strip()
    if username:
        exists = User.objects.filter(username=username).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False})

# ✅ Signup View
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()

        # Check for empty fields
        if not all([first_name, last_name, username, email, password1, password2]):
            messages.error(request, "All fields are required!")
            return render(request, 'signup.html', {'first_name': first_name, 'last_name': last_name, 'username': username, 'email': email})

        # Check for matching passwords
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html', {'first_name': first_name, 'last_name': last_name, 'username': username, 'email': email})

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return render(request, 'signup.html', {'first_name': first_name, 'last_name': last_name, 'email': email})

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return render(request, 'signup.html', {'first_name': first_name, 'last_name': last_name, 'username': username})

        # Validate password length and complexity
        if len(password1) < 8 or not re.search(r'\d', password1):
            messages.error(request, "Password must be at least 8 characters long and include a number.")
            return render(request, 'signup.html', {'first_name': first_name, 'last_name': last_name, 'username': username, 'email': email})

        # Create the user if everything is fine
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('signin')  # Redirect to login page after signup
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return render(request, 'signup.html', {'first_name': first_name, 'last_name': last_name, 'username': username, 'email': email})

    return render(request, 'signup.html')

# ✅ Signin View
def signin(request):
    next_url = request.GET.get('next', '')  # Keep track of any 'next' URL to redirect after login

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Username and password are required!")
            return render(request, 'signin.html')  # Show the error message on the same page

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect(next_url if next_url else 'home')  # Redirect to home or the next URL

        # If authentication fails, display an error message
        messages.error(request, "Invalid username or password.")
        return render(request, 'signin.html')  # Show the error message on the same page

    return render(request, 'signin.html', {'next': next_url})

# ✅ Logout View
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('signin')

# ✅ Home View
@login_required(login_url='signin')
def home(request):
    return render(request, "home.html")

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Use redirect instead of render for POST success
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def signin_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect after successful login
    else:
        form = AuthenticationForm()
    
    return render(request, 'account/signin.html', {'form': form})


def home(request):
    return render(request, 'account/home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('signin')


from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import CustomUserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'blog/logged_out.html'

def home_view(request):
    return render(request, 'blog/home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog/home')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog/profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
        
    return render(request, 'blog/profile.html', {'form': form})
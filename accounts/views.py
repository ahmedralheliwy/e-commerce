from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('products:product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('core:home')

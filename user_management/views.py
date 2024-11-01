from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomLoginForm
from .models import CustomUser

#def user_dashboard(request):
   # return HttpResponse("Welcome to the Student Registration System!")
def front_page(request):
    return render(request, 'user_management/base_generic.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('home')  # Redirect to a home or success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_management/register.html', {'form': form})


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile_update')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'user_management/profile_update.html', {'form': form})
def user_login(request):
    form = CustomLoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('root_redirect')  # Redirect to the home page or any other page
    return render(request, 'user_management/login.html', {'form': form})
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_management/user_list.html', {'users': users})

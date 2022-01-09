from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from .models import Profile


# Create your views here.

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'The entered details are incorrect')
    context = {}
    return render(request, 'login.html', context)



def registerPage(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            
            messages.success(request, 'Account created successfully for ' + user)
            return redirect('customers:login-page')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('index')


def customerProfileView(request, pk):
    customer = User.objects.get(id=pk)
    current_user = request.user
    profile = Profile.objects.filter(name=current_user)
    context = {'customer':customer, 'profile':profile}
    return render(request, 'profile_view.html', context)
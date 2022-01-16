from asyncio.windows_events import NULL
from logging import NullHandler
from queue import Empty
from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.

def login_page(request):

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



def register_page(request):
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


def logout_page(request):
    logout(request)
    return redirect('index')


def customer_profile_view(request, pk):
    customer = User.objects.get(id=pk)
    current_user = request.user
    profile = Profile.objects.get(name=current_user)
    
    # The below will direct the customer to the update page if address is empty
    addy = Profile.objects.get(name=current_user).address1
    print(str(addy))
    if addy == None:
        return redirect('customers:customer-update', pk)
    # Loads the customers Profile Page
    else:
        context = {'customer':customer, 'profile':profile}
        return render(request, 'profile_view.html', context)

def customer_profile_update(request, pk):
    # Ensuring only staff can view amend page
    # if request.user.is_staff:
        # View for Updating Customer Details
        profile = User.objects.get(id=pk)
        current_user = request.user
        profile = Profile.objects.get(name=current_user)
        
        form = UpdateProfileForm(instance=profile)
        if request.method == 'POST':
            form = UpdateProfileForm(
                request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Provider Updated Successfully')
                form = UpdateProfileForm()
                return redirect('customers:customer-profile', pk)
        else:
            context = {'form': form}
            return render(request, 'profile_update.html', context)
        
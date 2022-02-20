from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateProfileForm, FeedbackForm, ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


def login_page(request):
    # Enables a registered customer to log in
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
    # Enables a New customer to register
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # Success message to appear
            messages.success(
                request, 'Account created successfully for ' + user)
            return redirect('customers:login-page')
    context = {'form':form}
    return render(request, 'register.html', context)


def logout_page(request):
    logout(request)
    return redirect('index')


def customer_profile_view(request, pk):
    current_user = request.user
    profile = Profile.objects.get(name=current_user)
    # Below will direct the customer to the update page if address is empty
    addy = Profile.objects.get(name=current_user).address1
    if addy == None:
        return redirect('customers:customer-update', pk)
    # Loads the customers Profile Page
    else:
        context = {'profile':profile}
        return render(request, 'profile_view.html', context)


def customer_profile_update(request, pk):
    # Ensuring only staff can view amend page
    # if request.user.is_staff:
        # View for Updating Customer Details
        # profile = User.objects.get(id=pk)
    current_user = request.user
    profile = Profile.objects.get(name=current_user)
    
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(
            request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Provider Updated Successfully')
            form = UpdateProfileForm()
            return redirect('customers:customer-profile', pk)
    else:
        context = {'form': form}
        return render(request, 'profile_update.html', context)

def customer_profile_delete(request, pk):
    # View to delete account
    current_user = request.user
    profile = Profile.objects.get(name=current_user)
    if request.method == "POST":
        Profile.delete(profile)
        User.delete(current_user)
        messages.success(request, 'Account Deleted Successfully')
        return redirect('customers:login-page')
    profile = UpdateProfileForm(instance=profile)
    context = {'profile': profile}
    return render(request, 'delete.html', context)

def customer_feedback(request):
    # Feedback form for customers
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your Feedback')
            return redirect('customers:customer-feedback')
        else:
            messages.error(request, 'Please conplete the form fully')
    else:
        form = FeedbackForm()
        context = {'form': form}
        return render(request, 'feedback.html', context)

def contact_us(request):
    # Feedback form for customers
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your query. You will recieve a response within 24hr')
            return redirect('customers:contact-us')
        else:
            messages.error(request, 'Please complete the form fully')
    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact_us.html', context)

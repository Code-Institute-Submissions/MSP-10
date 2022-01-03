from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# def login(request):
#     # form = UserCreationForm()
    
#     # if request.method == 'POST':
#     #     form = UserCreationForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
    
#     # context = {'form:form'}
#     return render(request, 'login.html', context)

# def login(request):
#     # Ensure page is not displayed to logged in user
#     # if request.user.is_authenticated:
#     #     return redirect('index')
#     # else:
#         # View for basic display of the login page
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             messages.info(request, 'The entered details are incorrect')
#     context = {}
#     return render(request, 'login.html', context)



def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'register.html', context)
   
    # form = RegisterForm()
    # if request.method == "POST":
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # messages.success(request, 'Account created successfully')
    #         # username = form.cleaned_data['username']
    #         # password = form.cleaned_data['password1']
    #         # user = authenticate(username=username, password=password)
    #         # login(request, user)
    #         return redirect('login')
    # else:
    #     form = RegisterForm()
    # return render(request, 'register.html', {
    #     'form': form,
    #      })
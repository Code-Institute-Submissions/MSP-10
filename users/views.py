from django.shortcuts import render

# Create your views here.

def login(request):
    # View for displaying the login page
    return render(request, 'information/about.html')

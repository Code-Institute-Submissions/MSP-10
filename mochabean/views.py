from django.shortcuts import render


def index(request):
    # View for displaying the landing page
    return render(request, 'index.html')
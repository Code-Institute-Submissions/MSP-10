from django.shortcuts import render


def index(request):
    # View for displaying the landing page
    return render(request, 'index.html')

def policies(request):
    # View for displaying the resource list page
    return render(request, 'information/policies.html')

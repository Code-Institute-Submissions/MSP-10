from django.shortcuts import render


def index(request):
    # View for displaying the landing page
    return render(request, 'index.html')

def policies(request):
    # View for displaying the resource list page
    return render(request, 'information/policies.html')

def shipping(request):
    # View for displaying the resource list page
    return render(request, 'information/shipping.html')

def faq(request):
    # View for displaying the resource list page
    return render(request, 'information/faq.html')

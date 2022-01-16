from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import render, redirect
from subscriptions.forms import SubscriberForm
from subscriptions.models import newsletterSubscribers
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if newsletterSubscribers.objects.filter(email=instance.email).exists():
                messages.error(request, 'You are already subscribed')
            else:
                instance.save()
                messages.success(request, 'You are now Subscribed')
    form = SubscriberForm()
    context = {'form': form,}
    return render(request, 'index.html', context)


def policies(request):
    # View for displaying the policies page
    return render(request, 'information/policies.html')


def shipping(request):
    # View for displaying the shipping details page
    return render(request, 'information/shipping.html')


def faq(request):
    # View for displaying the faq page
    return render(request, 'information/faq.html')


def about(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if newsletterSubscribers.objects.filter(email=instance.email).exists():
                messages.error(request, 'You are already subscribed')
            else:
                instance.save()
                messages.success(request, 'You are now Subscribed')
    form = SubscriberForm()
    context = {'form': form,}
    return render(request, 'information/about.html', context)

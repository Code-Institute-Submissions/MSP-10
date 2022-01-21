import email
from django.shortcuts import render, redirect
from .models import newsletterSubscribers
from .forms import SubscriberForm
from django.contrib import messages

# Create your views here.

def newsletter_subscription_delete(request):
    # View to delete newsletter subscription
    form = SubscriberForm(request.POST)
    if request.method == "POST":
        # instance = form.save(commit=False)
        email1 = request.POST.get('email')
        if newsletterSubscribers.objects.filter(email=email1).exists():
            email_remove = newsletterSubscribers.objects.get(email=email1).pk
            newsletterSubscribers.delete(email_remove)
            messages.error(request, 'You have successfully unsubscribed')
            return redirect('index')
        else:
            messages.success(request, 'You were never subscribed!')
    context = {'form': form,}
    return render(request, 'unsubscribe.html', context)

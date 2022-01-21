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
        emailid = newsletterSubscribers.objects.filter(email=email1).values('id')
        if newsletterSubscribers.objects.filter(email=email1).exists():
            emailid.delete
            messages.error(request, 'You have successfully unsubscribed')
            return redirect('subscriptions:newsletter-unsubscribed')
        else:
            messages.success(request, 'You have never subscribed!')
    context = {'form': form,}
    return render(request, 'unsubscribe.html', context)

def newsletter_subscription_confirmation(request):
    # View for confirmation of Unsubscribing from newsletter
    return render(request, 'unsubscribe_confirm.html')

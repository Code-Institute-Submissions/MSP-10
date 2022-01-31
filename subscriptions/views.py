import email
from this import d
from django.shortcuts import render, redirect
from .models import newsletterSubscribers, CustomerSubscriptions
from .forms import SubscriberForm
from django.contrib import messages
import stripe
from decouple import config
import os


stripe.api_key = config('STRIPE_API_KEY')

# Create your views here.

def newsletter_subscription_delete(request):
    # View to delete newsletter subscription
    form = SubscriberForm(request.POST)
    if request.method == "POST":
        # instance = form.save(commit=False)
        email1 = request.POST.get('email')
        if newsletterSubscribers.objects.filter(email=email1).exists():
            emailid = newsletterSubscribers.objects.get(email=email1)
            emailid.delete()
            messages.error(request, 'You have successfully unsubscribed')
            return redirect('subscriptions:newsletter-unsubscribed')
        else:
            messages.success(request, 'You have never subscribed!')
    context = {'form': form,}
    return render(request, 'unsubscribe.html', context)


def newsletter_subscription_confirmation(request):
    # View for confirmation of Unsubscribing from newsletter
    return render(request, 'unsubscribe_confirm.html')


def product(request):
    return render(request, 'products.html')


def subscription_checkout(request):
    try:
        if request.user.customersubscriptions.membership:
            return redirect('settings')
    except CustomerSubscriptions.DoesNotExist:
        pass

    if request.method == 'POST':
        pass
    else:
        if request.method == 'GET' and 'membership' in request.GET:
            if request.GET['membership'] == 'PlanA':
                membership_id = 'price_1KNeD2BAHJm9GG3TRdiOiyyn'
                final_dollar = 19.95
                membership = 'I like to Dabble'
            
            if request.GET['membership'] == 'PlanB':
                membership_id = 'price_1KNeDIBAHJm9GG3T3un40z3y'
                final_dollar = 29.95
                membership = 'Finely Balanced'
            
            if request.GET['membership'] == 'PlanC':
                membership_id = 'price_1KNeFDBAHJm9GG3TwExvJshS'
                final_dollar = 39.95
                membership = 'Sleep is for the Weak'

        # Create Stripe Checkout
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email = request.user.email,
            line_items=[{
                'price': membership_id,
                'quantity': 1,
            }],
            mode='subscription',
            allow_promotion_codes=False,
            success_url='http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:8000/cancel',
        )

        return render(request, 'checkout.html', {'final_dollar': final_dollar, 'session_id': session.id})


def subscription_success(request):
    if request.method == 'GET' and 'session_id' in request.GET:
        session = stripe.checkout.Session.retrieve(request.GET['session_id'],)
        customer = CustomerSubscriptions()
        customer.user = request.user
        customer.stripeid = session.customer
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = session.subscription
        customer.save()
    return render(request, 'success.html')

def subscription_cancel(request):
    # View for cancelling payment
    return render(request, 'cancel.html')

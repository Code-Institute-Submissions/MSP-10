from django.shortcuts import render, redirect
from .models import newsletterSubscribers, CustomerSubscriptions
from .forms import SubscriberForm
from django.contrib import messages
from django.views import View
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY

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


# class CreateCheckoutSessionView(View):
#     def post(self, request, *args, **kwargs):
#         price = Price.objects.get(id=self.kwargs["pk"])
#         YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price': price.stripe_price_id,
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return redirect(checkout_session.url)

# class CreateCheckoutSession(View):
#     def post(self, request, *args, **kwargs):
#         if request.GET['membership'] == 'PlanA':
#             membership_id = 'price_1KNeD2BAHJm9GG3TRdiOiyyn'
#             price = 19.95
#             membership = 'I like to Dabble'
        
#         if request.GET['membership'] == 'PlanB':
#             membership_id = 'price_1KNeDIBAHJm9GG3T3un40z3y'
#             price = 29.95
#             membership = 'Finely Balanced'
        
#         if request.GET['membership'] == 'PlanC':
#             membership_id = 'price_1KNeFDBAHJm9GG3TwExvJshS'
#             price = 39.95
#             membership = 'Sleep is for the Weak'
            
#         YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'membership': CustomerSubscriptions.membership,
#                     'price': CustomerSubscriptions.price,
#                 },
#             ],
#             mode='subscription',
#             success_url=YOUR_DOMAIN + '/subscription/success/',
#             cancel_url=YOUR_DOMAIN + '/subscription/cancel/',
#         )
#         return redirect(checkout_session.url)


def subscription_checkout(request, membership):
    if request.method == 'POST':
        pass
    else:
        if request.method == 'GET' and 'membership' in request.GET:
            if request.GET['membership'] == 'PlanA':
                stripe_subscription_id = 'price_1KNeD2BAHJm9GG3TRdiOiyyn'
                price = 19.95
                membership = 'I like to Dabble'
            
            if request.GET['membership'] == 'PlanB':
                stripe_subscription_id = 'price_1KNeDIBAHJm9GG3T3un40z3y'
                price = 29.95
                membership = 'Finely Balanced'
            
            if request.GET['membership'] == 'PlanC':
                stripe_subscription_id = 'price_1KNeFDBAHJm9GG3TwExvJshS'
                price = 39.95
                membership = 'Sleep is for the Weak'

        context = {'price':price, 'membership': membership}
        return render(request, context)


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

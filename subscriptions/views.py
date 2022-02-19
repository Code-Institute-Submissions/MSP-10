from django.shortcuts import render, redirect
from .models import newsletterSubscribers, CustomerSubscriptions, Subscription
from .forms import SubscriberForm, SubscriptionCreate
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponseRedirect
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
        email1 = request.POST.get('email')
        if newsletterSubscribers.objects.filter(email=email1).exists():
            emailid = newsletterSubscribers.objects.get(email=email1)
            emailid.delete()
            messages.error(request, 'You have successfully unsubscribed')
            return redirect('subscriptions:newsletter-unsubscribed')
        else:
            messages.success(request, 'You have never subscribed!')
    context = {'form': form,}
    return render(request, 'newsletter/unsubscribe.html', context)


def newsletter_subscription_confirmation(request):
    # View for confirmation of Unsubscribing from newsletter
    return render(request, 'newsletter/unsubscribe_confirm.html')


def product(request):
    return render(request, 'products.html')

def product_create(request):
    # Ensuring only staff can view create page
    # if request.user.is_staff:
        # View for creating a New Provider on the site
    if request.method == 'POST':
        form = SubscriptionCreate(request.POST)
        if form.is_valid():
            form.save()
            #product = form.cleaned_data.get('name')
            messages.success(request, ' Created Successfully')
            return redirect('subscriptions:subscription-products')
        else:
            messages.error(request, 'New Product NOT Created Successfully')
    else:
        form = SubscriptionCreate()
    return render(request, 'products/create_subscription.html', {'form': form})
    # else:
    #     return redirect('index')


def product_update(request, pk):
    # Ensuring only staff can view amend page
# if request.user.is_staff:
    # View for Updating an existing Provider
    product = Subscription.objects.get(id=pk)
    form = SubscriptionCreate(instance=product)
    if request.method == 'POST':
        form = SubscriptionCreate(
            request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated Successfully, Remember to update Stripe')
            form = SubscriptionCreate()
            return redirect('subscriptions:subscription-products')
    context = {'form': form}
    return render(request, 'products/update_subscription.html', context)
# else:
#     return redirect('index')























# def subscription_checkout(request, membership):
#     if request.method == 'POST':
#         pass
#     else:
#         if request.method == 'GET' and 'membership' in request.GET:
#             if request.GET['membership'] == 'PlanA':
#                 stripe_subscription_id = 'price_1KNeD2BAHJm9GG3TRdiOiyyn'
#                 price = 19.95
#                 membership = 'I like to Dabble'
            
#             if request.GET['membership'] == 'PlanB':
#                 stripe_subscription_id = 'price_1KNeDIBAHJm9GG3T3un40z3y'
#                 price = 29.95
#                 membership = 'Finely Balanced'
            
#             if request.GET['membership'] == 'PlanC':
#                 stripe_subscription_id = 'price_1KNeFDBAHJm9GG3TwExvJshS'
#                 price = 39.95
#                 membership = 'Sleep is for the Weak'

#         context = {'price':price, 'membership': membership}
#         return render(request, context)


# def subscription_success(request):
#     if request.method == 'GET' and 'session_id' in request.GET:
#         session = stripe.checkout.Session.retrieve(request.GET['session_id'],)
#         customer = CustomerSubscriptions()
#         customer.user = request.user
#         customer.stripeid = session.customer
#         customer.membership = True
#         customer.cancel_at_period_end = False
#         customer.stripe_subscription_id = session.subscription
#         customer.save()
#     return render(request, 'success.html')

# def subscription_cancel(request):
#     # View for cancelling payment
#     return render(request, 'cancel.html')

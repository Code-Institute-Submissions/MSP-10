from django.shortcuts import render, redirect
from django.views.generic import ListView
from crispy_forms.helper import FormHelper
from .models import newsletterSubscribers, Subscription, CustomerSubscriptions
from customers.models import Profile
from .forms import SubscriberForm, SubscriptionCreate
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


####################################################
# Views in relation to the newsletter subscription #
####################################################


def newsletter_subscription_delete(request):
    # View to request to delete newsletter subscription
    form = SubscriberForm(request.POST)
    if request.method == "POST":
        email1 = request.POST.get("email")
        if newsletterSubscribers.objects.filter(email=email1).exists():
            emailid = newsletterSubscribers.objects.get(email=email1)
            emailid.delete()
            messages.error(request, "You have successfully unsubscribed")
            return redirect("subscriptions:newsletter-unsubscribed")
        else:
            messages.success(request, "You have never subscribed!")
    context = {
        "form": form,
    }
    return render(request, "newsletter/unsubscribe.html", context)


def newsletter_subscription_confirmation(request):
    # View for confirmation of Unsubscribing from newsletter
    return render(request, "newsletter/unsubscribe_confirm.html")


########################################################
# Views in relation to Product maintenance on the site #
########################################################


class product(ListView):
    # View all available Subscription Products
    model = Subscription
    template_name = "products.html"
    ordering = ["price"]


def product_create(request):
    # Ensuring only staff can view create page
    if request.user.is_staff:
        # View for creating a New Subscription product
        if request.method == "POST":
            form = SubscriptionCreate(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, " Created Successfully")
                return redirect("subscriptions:subscription-products")
            else:
                messages.error(request, "New Product NOT Created Successfully")
        else:
            form = SubscriptionCreate()
        return render(
            request,
            "products/create_subscription.html",
            {"form": form})
    else:
        return redirect("index")


def product_update(request, pk):
    # Ensuring only staff can view amend page
    if request.user.is_staff:
        # View for Updating an existing Provider
        product = Subscription.objects.get(id=pk)
        form = SubscriptionCreate(instance=product)
        if request.method == "POST":
            form = SubscriptionCreate(request.POST, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, "Product Updated Successfully")
                return redirect("subscriptions:subscription-products")
        context = {"form": form}
        return render(request, "products/update_subscription.html", context)
    else:
        return redirect("index")


def product_delete(request, pk):
    # Ensuring only staff can view delete page
    if request.user.is_staff:
        # View to delete an existing Product
        product = Subscription.objects.get(id=pk)
        if request.method == "POST":
            Subscription.delete(product)
            messages.success(request, "Product Deleted Successfully")
            return redirect("subscriptions:subscription-products")
        context = {"product": product}
        return render(request, "products/delete_subscription.html", context)
    else:
        return redirect("index")


#################################
# Views in relation to Payments #
#################################


def subscription_checkout(request, pk):
    # Verifies that user profile details are up to date
    current_user = request.user
    profile = Profile.objects.get(name=current_user)
    # Below will direct the customer to the update page if address is empty
    addy = Profile.objects.get(name=current_user).address1
    if addy is None:
        return redirect("customers:customer-update", pk)
    # Loads the customers Profile Page
    else:
        # Enables the checkout process
        product = Subscription.objects.get(id=pk)
        context = {"product": product}
        return render(request, "checkout.html", context)


def subscription_success(request, pk):
    # Populates HTML screen with users selection
    # Creates entry on CustomerSubscriptions model
    product = Subscription.objects.get(id=pk)
    user = request.user
    subscript = product.stripe_subscription_id
    customer_sub = CustomerSubscriptions.objects.create(
        user=user, stripe_subscription_id=subscript
    )
    context = {"product": product}
    return render(request, "success.html", context)


def subscription_unsuccess(request):
    # Page displayed when payment is unsuccessful
    return render(request, "unsuccess.html")


def customer_subscription(request):
    # Populates the users chosen subscription
    current_user = request.user
    customer = CustomerSubscriptions.objects.get(user=current_user)
    plan = customer.stripe_subscription_id
    product = Subscription.objects.get(stripe_subscription_id=plan)
    context = {"product": product}
    return render(request, "customer_subscription.html", context)

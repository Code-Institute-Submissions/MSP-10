from django.test import TestCase
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from . import views


class NewsletterUnsubscribeTests(SimpleTestCase):
    # Status check of the unsubscribe page
    def test_newsletter_unsubscribe_status(self):
        response = self.client.get('/unsubscribe/')
        self.assertEquals(response.status_code, 200)

    def test_newsletter_unsubscribe_by_name(self):
        response = self.client.get(
            reverse('subscriptions:newsletter-unsubscribe'))
        self.assertEquals(response.status_code, 200)

    def test_newsletter_unsubscribe_template(self):
        response = self.client.get(
            reverse('subscriptions:newsletter-unsubscribe'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/unsubscribe.html')


class NewsletterUnsubscribeConfirmTests(SimpleTestCase):
    # Status check of the unsubscribed confirm page
    def test_newsletter_unsubscribed_status(self):
        response = self.client.get('/unsubscribed/')
        self.assertEquals(response.status_code, 200)

    def test_newsletter_unsubscribed_by_name(self):
        response = self.client.get(
            reverse('subscriptions:newsletter-unsubscribed'))
        self.assertEquals(response.status_code, 200)

    def test_newsletter_unsubscribed_template(self):
        response = self.client.get(
            reverse('subscriptions:newsletter-unsubscribed'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'newsletter/unsubscribe_confirm.html')


class SubscriptionProductsTests(TestCase):
    # Status check of the unsubscribed confirm page
    def test_subscription_products_status(self):
        response = self.client.get('/subscription/products/')
        self.assertEquals(response.status_code, 200)

    def test_subscription_products_by_name(self):
        response = self.client.get(
            reverse('subscriptions:subscription-products'))
        self.assertEquals(response.status_code, 200)

    def test_subscription_products_template(self):
        response = self.client.get(reverse(
            'subscriptions:subscription-products'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

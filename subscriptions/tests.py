from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from . import views


class NewsletterUnsubscribeTests(SimpleTestCase):
    # Status check of the unsubscribe page
    def test_newsletter_unsubscribe_status(self):
        response = self.client.get('/unsubscribe/')
        self.assertEquals(response.status_code, 200)

    def test_newsletter_unsubscribe_by_name(self):
        response = self.client.get(reverse('subscriptions:newsletter-unsubscribe'))
        self.assertEquals(response.status_code, 200)

    def test_newsletter_unsubscribe_template(self):
        response = self.client.get(reverse('subscriptions:newsletter-unsubscribe'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'unsubscribe.html')

class NewsletterUnsubscribeConfirmTests(SimpleTestCase):
    # Status check of the unsubscribed confirm page
    def test_newsletter_unsubscribed_status(self):
        response = self.client.get('/unsubscribed/')
        self.assertEquals(response.status_code, 200)

    def test_newsletter_unsubscribed_by_name(self):
        response = self.client.get(reverse('subscriptions:newsletter-unsubscribed'))
        self.assertEquals(response.status_code, 200)

    def test_newsletter_unsubscribed_template(self):
        response = self.client.get(reverse('subscriptions:newsletter-unsubscribed'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'unsubscribe_confirm.html')
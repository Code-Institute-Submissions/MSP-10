from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from . import views


class HomePageTests(SimpleTestCase):
    # Status check of the websites landing page
    def test_home_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class PoliciesPageTests(SimpleTestCase):
    # Status check of the websites policies page
    def test_policies_page_status(self):
        response = self.client.get('/policies/')
        self.assertEquals(response.status_code, 200)

    def test_policies_page_by_name(self):
        response = self.client.get(reverse('policies'))
        self.assertEquals(response.status_code, 200)

    def test_policies_page_template(self):
        response = self.client.get(reverse('policies'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/policies.html')


class ShippingPageTests(SimpleTestCase):
    # Status check of the websites shipping page
    def test_shipping_page_status(self):
        response = self.client.get('/shipping/')
        self.assertEquals(response.status_code, 200)

    def test_shipping_page_by_name(self):
        response = self.client.get(reverse('shipping'))
        self.assertEquals(response.status_code, 200)

    def test_shipping_page_template(self):
        response = self.client.get(reverse('shipping'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/shipping.html')


class FAQPageTests(SimpleTestCase):
    # Status check of the websites faq page
    def test_faq_page_status(self):
        response = self.client.get('/faq/')
        self.assertEquals(response.status_code, 200)

    def test_faq_page_by_name(self):
        response = self.client.get(reverse('faq'))
        self.assertEquals(response.status_code, 200)

    def test_faq_page_template(self):
        response = self.client.get(reverse('faq'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/faq.html')


class AboutPageTests(SimpleTestCase):
    # Status check of the websites about page
    def test_about_page_status(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_about_page_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_about_page_template(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/about.html')

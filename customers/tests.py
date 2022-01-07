from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls.base import reverse_lazy


class TestCustomerRegistrationPageTests(TestCase):
    # Test for the customer registration page load
    def test_registration_page_status_code(self):
        response = self.client.get('/customers/register/')
        self.assertEquals(response.status_code, 200)

    def test_registration_url_by_name(self):
        response = self.client.get(reverse('customers:register-page'))
        self.assertEquals(response.status_code, 200)

    def test_registration_uses_correct_template(self):
        response = self.client.get(reverse('customers:register-page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

class TestCustomerLoginPageTests(TestCase):
    # Test for the customer login page load
    def test_login_page_status_code(self):
        response = self.client.get('/customers/login/')
        self.assertEquals(response.status_code, 200)

    def test_login_url_by_name(self):
        response = self.client.get(reverse('customers:login-page'))
        self.assertEquals(response.status_code, 200)

    def test_login_uses_correct_template(self):
        response = self.client.get(reverse('customers:login-page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

class TestCustomerRegister(TestCase):
    # Test Customer Registration
    def test_register_customer(self):
        response = self.client.post(reverse('customers:register-page'), data={
            'username': 'TestRegister',
            'email': 'register@test.com',
            'password1': 'a1b2c3d4',
            'password2': 'a1b2c3d4'
        })
        self.assertEqual(response.status_code, 200)


class TestCustomerLogin(TestCase):
    # Test customer login
    def test_member_signin(self):
        response = self.client.post(reverse('customers:login-page'), data={
            'username': 'TestRegister',
            'password1': 'a1b2c3d4',
        })
        self.assertEqual(response.status_code, 200)
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


class TestResetPasswordTests(TestCase):
    # Test for the customer reset_password load
    def test_reset_password_status_code(self):
        response = self.client.get('/customers/reset_password/')
        self.assertEquals(response.status_code, 200)

    def test_reset_password_url_by_name(self):
        response = self.client.get(reverse('customers:reset_password'))
        self.assertEquals(response.status_code, 200)

    def test_reset_password_uses_correct_template(self):
        response = self.client.get(reverse('customers:reset_password'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'password/password_reset_form.html')


class TestResetPasswordSentTests(TestCase):
    # Test for the customer reset_password sent
    def test_reset_password_sent_status_code(self):
        response = self.client.get('/customers/reset_password_sent/')
        self.assertEquals(response.status_code, 200)

    def test_reset_password_sent_url_by_name(self):
        response = self.client.get(reverse('customers:password_reset_done'))
        self.assertEquals(response.status_code, 200)

    def test_reset_password_sent_uses_correct_template(self):
        response = self.client.get(reverse('customers:password_reset_done'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'password/password_reset_done.html')


class TestResetPasswordCompleteTests(TestCase):
    # Test for the customer reset_password complete
    def test_reset_password_complete_status_code(self):
        response = self.client.get('/customers/reset_password_complete/')
        self.assertEquals(response.status_code, 200)

    def test_reset_password_complete_url_by_name(self):
        response = self.client.get(
            reverse('customers:password_reset_complete'))
        self.assertEquals(response.status_code, 200)

    def test_reset_password_complete_uses_correct_template(self):
        response = self.client.get(
            reverse('customers:password_reset_complete'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'password/password_reset_complete.html')


class TestCustomerFeedbackTests(TestCase):
    # Test for the customer reset_password complete
    def test_customer_feedback_status_code(self):
        response = self.client.get('/customers/feedback/')
        self.assertEquals(response.status_code, 200)

    def test_customer_feedback_url_by_name(self):
        response = self.client.get(reverse('customers:customer-feedback'))
        self.assertEquals(response.status_code, 200)

    def test_customer_feedback_uses_correct_template(self):
        response = self.client.get(reverse('customers:customer-feedback'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback.html')

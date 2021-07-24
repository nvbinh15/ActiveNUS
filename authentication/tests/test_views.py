from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages


class TestViews(TestCase):
    def test_should_show_register_page(self):
        response = self.client.get(reverse('auth_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")

    def test_should_show_login_page(self):
        response = self.client.get(reverse('auth_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")

    def test_should_signup_user(self):
        self.user = {
            "username": "username",
            "email": "email@hmail2.com",
            "password1": "password",
            "password2": "password"
        }
        response = self.client.post(reverse("auth_register"), self.user)
        self.assertEquals(response.status_code, 302)

    def test_should_not_signup_user_with_taken_username(self):

        self.user = {
            "username": "username",
            "email": "email@hmail2.com",
            "password1": "password",
            "password2": "password"
        }

        self.client.post(reverse("auth_register"), self.user)
        response = self.client.post(reverse("auth_register"), self.user)
        self.assertEquals(response.status_code, 409)

        storage = get_messages(response.wsgi_request)

        self.assertIn("Username is taken, choose another one",
                      list(map(lambda x: x.message, storage)))

    def test_should_not_signup_user_with_taken_email(self):

        self.user = {
            "username": "username1",
            "email": "email@hmail2.com",
            "password1": "password",
            "password2": "password"
        }

        self.test_user2 = {
            "username": "username11",
            "email": "email@hmail2.com",
            "password1": "password",
            "password2": "password"
        }

        self.client.post(reverse("auth_register"), self.user)
        response = self.client.post(reverse("auth_register"), self.test_user2)
        self.assertEquals(response.status_code, 409)

    
    def test_should_not_signup_user_with_mismatch_passwords(self):

        self.user = {
            "username": "username3",
            "email": "email@hmail3.com",
            "password1": "password3",
            "password2": "password33"
        }

        self.client.post(reverse("auth_register"), self.user)
        response = self.client.post(reverse("auth_register"), self.user)
        self.assertEquals(response.status_code, 409)

        storage = get_messages(response.wsgi_request)

        self.assertIn("Password mismatch",
                      list(map(lambda x: x.message, storage)))

from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages


class TestViews(TestCase):
    def test_home_page_redirect_login(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(
            response, 
            expected_url='/auth/login?next=/',
            status_code=302, 
            target_status_code=200, 
            msg_prefix='', 
            fetch_redirect_response=True
        )


    def test_pomodoro_redirect_login(self):
        response = self.client.get(reverse('pomodoro'))
        self.assertRedirects(
            response, 
            expected_url='/auth/login?next=/pomodoro',
            status_code=302, 
            target_status_code=200, 
            msg_prefix='', 
            fetch_redirect_response=True
        )


    def test_calendar_redirect_login(self):
        response = self.client.get(reverse('calendar'))
        self.assertRedirects(
            response, 
            expected_url='/auth/login?next=/calendar',
            status_code=302, 
            target_status_code=200, 
            msg_prefix='', 
            fetch_redirect_response=True
        )

    def test_flashcard_redirect_login(self):
        response = self.client.get(reverse('flashcard'))
        self.assertRedirects(
            response, 
            expected_url='/auth/login?next=/flashcard',
            status_code=302, 
            target_status_code=200, 
            msg_prefix='', 
            fetch_redirect_response=True
        )






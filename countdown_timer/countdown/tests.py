from django.test import TestCase
from .forms import TimerForm

class TimerFormTests(TestCase):
    def test_valid_form(self):
        form = TimerForm(data={'hours': 0, 'minutes': 1, 'seconds': 30})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = TimerForm(data={'hours': 0, 'minutes': 0, 'seconds': 0})
        self.assertFalse(form.is_valid())

class CountdownViewTests(TestCase):
    def test_view_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Countdown Timer")
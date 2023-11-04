from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(username='testuser', password='testpass')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('restaurant:index'), follow=True)
        self.assertEqual(response.status_code, 200)

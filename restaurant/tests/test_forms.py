from django.test import TestCase
from restaurant.forms import DishForm
from restaurant.models import Cook, DishType


class DishFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        DishType.objects.create(name='Dessert')
        Cook.objects.create(username='john_doe')

    def test_form_validation_for_blank_items(self):
        form = DishForm(data={'name': '', 'description': '', 'price': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])

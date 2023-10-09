from django.test import TestCase
from restaurant.models import Dish, DishType


class DishModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        DishType.objects.create(name='Dessert')
        Dish.objects.create(name='Ice Cream', description='Vanilla Ice Cream',
                            price=5.00, dish_type=DishType.objects.get(name='Dessert'))

    def test_name_label(self):
        dish = Dish.objects.get(id=1)
        field_label = dish._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

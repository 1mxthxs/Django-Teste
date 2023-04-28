from django.test import TestCase
from django.urls import reverse, resolve


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEquals(url, '/')

    def test_recipe_category_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEquals(url, '/recipes/category/1/')

    def test_recipe_item_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEquals(url, '/recipes/1/')

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        
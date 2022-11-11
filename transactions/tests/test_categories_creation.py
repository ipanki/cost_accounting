from django.test import TestCase
from django.contrib.auth.models import User


class CreateCategoriesTestCase(TestCase):
    def test_create_categories(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.assertEqual(11, self.user.categories.count())

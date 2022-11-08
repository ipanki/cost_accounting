from django.conf import settings

from transactions.models import Category


def adding_categories(user):
    for category in settings.DEFAULT_CATEGORIES:
        Category.objects.create(name=category, user=user)

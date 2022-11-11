from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from transactions.models import Category


@receiver(post_save, sender=User)
def add_categories(sender, instance, created, **kwargs):
    if created:
        for category in settings.DEFAULT_CATEGORIES_NAME:
            Category.objects.create(name=category, user=instance)

from django.conf import settings
from django.db import models
from django.db.models import BigIntegerField


class Category(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="categories")


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="transactions")
    organization = models.CharField(max_length=30)
    amount = BigIntegerField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    income = models.BooleanField(default=False)

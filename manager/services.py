from django.shortcuts import get_object_or_404

from manager.models import Tag
from django.contrib.auth.models import User


def adding_categories(user):
    default_categories = ("Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина", "Образование",
                          "Отдых и развлечения", "Платежи, комиссии", "Покупки: одежда, техника", "Продукты", "Проезд")
    for category in default_categories:
        new_user = get_object_or_404(User, username=user)
        Tag.objects.create(name=category, user=new_user)

from django.urls import path, include
from rest_framework import routers
from transactions import catogories_views, transactions_views

router = routers.DefaultRouter()
router.register('categories', catogories_views.CategoriesViewSet, 'categories')
router.register('accounting', transactions_views.TransactionsViewSet, 'accounting')

urlpatterns = [
    path('', include((router.urls, 'categories'), namespace='categories')),
    path('', include((router.urls, 'accounting'), namespace='accounting')),

]

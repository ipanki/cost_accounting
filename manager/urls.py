from django.urls import path, include
from rest_framework import routers
from manager import registration_views, catogories_views, transactions_views

router = routers.DefaultRouter()
router.register('manager', registration_views.RegistrationViewSet, 'manager')
router.register('categories', catogories_views.CategoriesViewSet, 'categories')
router.register('accounting', transactions_views.TransactionsViewSet, 'accounting')

urlpatterns = [
    path('', include((router.urls, 'signup'), namespace='profiles')),
    path('', include((router.urls, 'categories'), namespace='categories')),
    path('', include((router.urls, 'accounting'), namespace='accounting')),

]

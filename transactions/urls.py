from django.urls import path, include
from rest_framework import routers
from transactions import views

router = routers.DefaultRouter()
router.register('categories', views.CategoriesViewSet, 'categories')
router.register('transactions', views.TransactionsViewSet, 'accounting')

urlpatterns = [
    path('', include((router.urls, 'categories'), namespace='categories')),
    path('', include((router.urls, 'accounting'), namespace='accounting')),

]

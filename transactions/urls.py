from django.urls import include, path
from rest_framework import routers

from transactions import views

router = routers.DefaultRouter()
router.register('categories', views.CategoriesViewSet, 'categories')
router.register('transactions', views.TransactionsViewSet, 'accounting')
router.register('report', views.ReportsViewSet, 'report')

urlpatterns = [
    path('', include(router.urls)),

]

from django.urls import include, path
from rest_framework import routers

from authentication import views

router = routers.DefaultRouter()
router.register('auth', views.RegistrationViewSet, 'auth')

urlpatterns = [
    path('', include((router.urls, 'signup'), namespace='auth')),

]

from django.urls import path, include
from rest_framework import routers
from authentication import registration_views

router = routers.DefaultRouter()
router.register('auth', registration_views.RegistrationViewSet, 'auth')

urlpatterns = [
    path('', include((router.urls, 'signup'), namespace='auth')),

]

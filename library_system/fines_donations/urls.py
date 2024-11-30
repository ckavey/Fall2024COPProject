from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FineViewSet, DonationViewSet
from django.urls import path
from .views import create_payment_intent

router = DefaultRouter()
router.register(r'fines', FineViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns += [
    path('create-payment-intent/', create_payment_intent, name='create-payment-intent'),
]

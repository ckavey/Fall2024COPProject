from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FineViewSet, DonationViewSet, create_payment_intent

# Initialize the API router
router = DefaultRouter()
router.register(r'fines', FineViewSet)
router.register(r'donations', DonationViewSet)

# Define app-specific urlpatterns
urlpatterns = [
    path('api/', include(router.urls)),  # API endpoints for fines and donations
    path('create-payment-intent/', create_payment_intent, name='create-payment-intent'),  # Payment intent
    ]


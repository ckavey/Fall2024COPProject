from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse
import stripe
from .models import Fine, Donation
from .serializers import FineSerializer, DonationSerializer

# Initialize Stripe with secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

# ViewSet for Fine model
class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer

# ViewSet for Donation model
class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def get_serializer_context(self):
        return {'request': self.request}

# API to handle Stripe Payment Intent
@api_view(['POST'])
def create_payment_intent(request):
    try:
        # Get the amount from the request data
        amount = request.data.get('amount')
        if not amount:
            return Response({'error': 'Amount is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Convert the amount to cents
        amount_in_cents = int(float(amount) * 100)

        # Create PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency='usd',
            payment_method_types=['card'],
        )
        return Response({'clientSecret': intent['client_secret']})
    except stripe.error.StripeError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# API to handle user signup
@api_view(['POST'])
def signup(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=email).exists():
        return Response({'error': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=email, email=email, password=password)
    user.save()
    return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)

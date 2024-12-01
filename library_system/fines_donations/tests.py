from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Fine, Donation


class FineAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.fine = Fine.objects.create(
            user=self.user,
            amount=20.00,
            description="Initial fine for testing",
            due_date=now() + timedelta(days=7)
        )

    def test_get_fines(self):
        response = self.client.get('/api/fines/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_specific_fine(self):
        response = self.client.get(f'/api/fines/{self.fine.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.fine.id)

    def test_create_fine(self):
        data = {
            "user": self.user.id,
            "amount": 30.00,
            "description": "Overdue book fine",
            "due_date": (now() + timedelta(days=14)).strftime('%Y-%m-%d')
        }
        response = self.client.post('/api/fines/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Fine.objects.count(), 2)


class DonationAPITest(APITestCase):
    def setUp(self):
        # Set up a user for authentication
        self.user = User.objects.create_user(username='donor', password='testpass')
        self.client.force_authenticate(user=self.user)  # Authenticate the test client

        # Create a sample donation
        self.donation = Donation.objects.create(
            user=self.user,
            amount=50.00,
            message="Keep up the great work!"
        )

    def test_get_donations(self):
        # Test fetching all donations
        response = self.client.get('/api/donations/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_donation_invalid_amount(self):
        data = {
            "user": self.user.id,
            "amount": -50.00,  # Invalid amount
            "message": "Invalid donation"
        }
        response = self.client.post('/api/donations/', data, format='json')
        self.assertEqual(response.status_code, 400)

        data = {
            "user": self.user.id,
            "amount": 0.00,  # Invalid amount
            "message": "Invalid donation"
        }
        response = self.client.post('/api/donations/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_donation_invalid(self):
        # Test creating a donation with invalid data
        data = {"amount": "invalid_amount"}
        response = self.client.post('/api/donations/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_delete_donation(self):
        # Test deleting a donation
        response = self.client.delete(f'/api/donations/{self.donation.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Donation.objects.count(), 0)


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="testuser@example.com",
                                             password="testpassword123")

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

    def test_user_authentication(self):
        login = self.client.login(username="testuser", password="testpassword123")
        self.assertTrue(login)

    def test_inactive_user_authentication(self):
        self.user.is_active = False
        self.user.save()
        login = self.client.login(username="testuser", password="testpassword123")
        self.assertFalse(login)

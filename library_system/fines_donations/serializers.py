from rest_framework import serializers
from django.utils.timezone import now
from .models import Fine, Donation


# Serializer for the Fine model
class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = '__all__'  # Serializes all fields in the Fine model

    def validate_due_date(self, value):
        if value < now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value


# Serializer for the Donation model
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'amount', 'message', 'date_donated', 'user']
        read_only_fields = ['user']  # Make 'user' a read-only field

    def create(self, validated_data):
        # Automatically assign the authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
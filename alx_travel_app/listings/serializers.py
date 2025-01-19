from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """Serializer for the Listing model"""
    
    class Meta:
        model = Listing
        fields = '__all__'  # Includes all fields


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for the Booking model"""
    
    class Meta:
        model = Booking
        fields = '__all__'  # Includes all fields

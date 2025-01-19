from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

### LISTINGS CRUD ###

@swagger_auto_schema(
    method='get',
    responses={200: ListingSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    request_body=ListingSerializer,
    responses={201: ListingSerializer}
)
@api_view(['GET', 'POST'])
def listing_list_create(request):
    """Retrieve all listings or create a new listing"""
    if request.method == 'GET':
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={200: ListingSerializer}
)
@swagger_auto_schema(
    method='put',
    request_body=ListingSerializer,
    responses={200: ListingSerializer}
)
@swagger_auto_schema(
    method='delete',
    responses={204: 'No Content'}
)
@api_view(['GET', 'PUT', 'DELETE'])
def listing_detail(request, pk):
    """Retrieve, update, or delete a listing by ID"""
    try:
        listing = Listing.objects.get(pk=pk)
    except Listing.DoesNotExist:
        return Response({"error": "Listing not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListingSerializer(listing)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


### BOOKINGS CRUD ###

@swagger_auto_schema(
    method='get',
    responses={200: BookingSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    request_body=BookingSerializer,
    responses={201: BookingSerializer}
)
@api_view(['GET', 'POST'])
def booking_list_create(request):
    """Retrieve all bookings or create a new booking"""
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={200: BookingSerializer}
)
@swagger_auto_schema(
    method='put',
    request_body=BookingSerializer,
    responses={200: BookingSerializer}
)
@swagger_auto_schema(
    method='delete',
    responses={204: 'No Content'}
)
@api_view(['GET', 'PUT', 'DELETE'])
def booking_detail(request, pk):
    """Retrieve, update, or delete a booking by ID"""
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

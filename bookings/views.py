from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django import forms
from django.contrib import messages
import uuid
from .forms import CreateBookingForm
from .models import EventBooking
from django.contrib.auth.decorators import login_required


# Create a booking
def process_form(request):
    form = CreateBookingForm()
    #bookable_times = ["07:30", "20:00"]

    if request.method == 'POST':
        form = CreateBookingForm(request.POST)
        if form.is_valid():
                    booking = form.save(commit=False)
                    booking.user = request.user
                    booking.save()
                    messages.info(request, 'You have placed a booking.')
                    return redirect('my_bookings')
            
    return render(request, 'bookings/process_form.html', {'form': form})


# Show bookings
@login_required
def my_bookings(request):
    
    booking = EventBooking.objects.filter(user=request.user)
    form = CreateBookingForm()
    context = {
    'bookings': booking, 
    }
    return render(request, 'bookings/my_bookings.html', context)

#Update booking
def edit_item(request, booking_id):
    bookings = get_object_or_404(EventBooking, booking_id=booking_id)
    form = CreateBookingForm(instance=bookings)
    context = {
    'bookings': bookings,
    'form': form
 }

    if request.method == 'POST':
        form = CreateBookingForm(request.POST, instance=bookings)
        if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.info(request, 'You have updated a booking.')
                return redirect('my_bookings')
            
    return render(request, 'bookings/edit_item.html', {'form': form})

# Delete booking
def delete_booking(request, booking_id):
    bookings = get_object_or_404(EventBooking, booking_id=booking_id)
    if request.method == 'POST':
        bookings.delete()
        messages.info(request, 'You have deleted your booking.')
        return redirect('my_bookings')
        
    return render(request, 'bookings/delete_booking.html', {'bookings': bookings})

#     # Din vykod här


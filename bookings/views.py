from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django import forms
from django.contrib import messages
import uuid
from .forms import CreateBookingForm
from .models import EventBooking

def process_form(request):
    form = CreateBookingForm()

    if request.method == 'POST':
        form = CreateBookingForm(request.POST)
        if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.info(request, 'You have placed a booking.')
                return redirect('my_bookings')
            
    return render(request, 'bookings/process_form.html', {'form': form})



def my_bookings(request):
    
    booking = EventBooking.objects.all()
    form = CreateBookingForm()
    context = {
    'bookings': booking, 
    }
    return render(request, 'bookings/my_bookings.html', context)


def edit_item(request, booking_id):
    bookings = get_object_or_404(EventBooking, booking_id=booking_id)
    form = CreateBookingForm(instance=bookings)
    context = {
    'bookings': bookings,
    'form': form
 }
    #return render(request, 'bookings/edit_item.html', context)

    if request.method == 'POST':
        form = CreateBookingForm(request.POST, instance=bookings)
        if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.info(request, 'You have updated a booking.')
                return redirect('my_bookings')
            
    return render(request, 'bookings/edit_item.html', {'form': form})


def delete_booking(request):
    bookings = EventBooking.objects.all()
    context = {
       'bookings': bookings
}
    return render(request, 'bookings/delete_booking.html', context)
#     # Din vykod här
#     return render(request, 'create_booking.html/')

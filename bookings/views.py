from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from .forms import CreateBookingForm
from .models import EventBooking
from django.contrib.auth.decorators import login_required


@login_required
def process_form(request):
    '''
    Create booking by user request. Checks if bookingis uniqe, if it is the booking will be saved.
    '''
    form = CreateBookingForm()

    if request.method == 'POST':
        form = CreateBookingForm(request.POST)
        if form.is_valid():
            event_date = form.cleaned_data['event_date']
            lesson_time = form.cleaned_data['lesson_time']
            stored_bookings = EventBooking.objects.filter(event_date = str(event_date), lesson_time = str(lesson_time))
            if stored_bookings.exists():
                messages.info(request, 'Chosen time and date have already been booked. Please try another time or date.')
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.info(request, 'You have placed a booking.')
                return redirect('my_bookings')
            
    return render(request, 'bookings/process_form.html', {'form': form})


@login_required
def my_bookings(request):
    '''
    Renders all bookings in my_bookings.html.
    '''
    booking = EventBooking.objects.filter(user=request.user)
    form = CreateBookingForm()
    context = {
    'bookings': booking, 
    }

    return render(request, 'bookings/my_bookings.html', context)


def edit_item(request, booking_id):
    '''
    Update a specific booking. Get the EventBooking object by it's id.
    
    '''
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


def delete_booking(request, booking_id):
    '''
    This functin will delete booking from database by user request.
    '''
    bookings = get_object_or_404(EventBooking, booking_id=booking_id)
    if request.method == 'POST':
        bookings.delete()
        messages.info(request, 'You have deleted your booking.')
        return redirect('my_bookings')
        
    return render(request, 'bookings/delete_booking.html', {'bookings': bookings})


    

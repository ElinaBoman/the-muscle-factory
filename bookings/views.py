from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django import forms
from django.contrib import messages
import uuid
from .forms import CreateBookingForm
from .models import EventBooking
from django.contrib.auth.decorators import login_required


'''
This function will take user request to create bookings. If all fields in the form has been filled in correctly, the
function will check if there is allready a booking with same date and time. If there is, the user will recive a info message
that suggests that the user selects different date or time. If there is no booking for chosen date and time the function will proceed and save the booking. 
'''
def process_form(request):
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


'''
This will collect the total bookigns that user has created.
'''
@login_required
def my_bookings(request):
    booking = EventBooking.objects.filter(user=request.user)
    form = CreateBookingForm()
    context = {
    'bookings': booking, 
    }

    return render(request, 'bookings/my_bookings.html', context)

'''
If theuser wants to update a specific booking this function will get the EventBooking object by it's id.
The user will be able to change the booking inside the CreateBookingForm, that has the autofill from earlier booking.
'''
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

'''
This functin will delete booking from database by user request.
'''
def delete_booking(request, booking_id):
    bookings = get_object_or_404(EventBooking, booking_id=booking_id)
    if request.method == 'POST':
        bookings.delete()
        messages.info(request, 'You have deleted your booking.')
        return redirect('my_bookings')
        
    return render(request, 'bookings/delete_booking.html', {'bookings': bookings})



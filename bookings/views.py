from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django import forms
from django.contrib import messages
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




# if request.method == 'POST':
#         form = proccess_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#         else:
#             form = process_form()


#         return render(request, 'bookings/process_form.html', {'form': form})


def my_bookings(request):
     bookings = EventBooking.objects.all()
     context = {
        'bookings': bookings
}
     return render(request, 'bookings/my_bookings.html', context)


#     # Din vykod här
#     return render(request, 'create_booking.html/')

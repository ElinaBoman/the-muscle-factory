from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# create BookinEvent render view
# class create_booking(View):
#     template_name = 'create_booking'


#     def get(self, request, *args, **kwargs):
#         form = createBookingForm()
#         return render(request, self.template_name, {"form":form})

#     def post(self, request, *args, **kwargs):
#         form = createBookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user = request.user
#             booking.save()
#             messages.info(request, 'Your lesson was booked successfully!')
#             return redirect('user_bookings')
        
#         return render(request, self.template_name, {'form': form})
def say_hello(request):
    return HttpResponse('Helloelle')

# def bookings(request):
#     """This function render the contact page of the project."""
#     return render(
#         request,
#         "create_booking.html")

def create_booking(request):
    # Din vykod här
    return render(request, 'create_booking.html/')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import userProfileForm

# Create your views here.


def userProfile_view(request):

    if request.method == 'POST':
        form = userProfileForm(request.POST)
        if form.is_valid():
            form.save
            messages.success(request, 'Your memberlevel has been updated!')
            return redirect('home')
    else:
        # Om förfrågan inte är en POST-förfrågan, skapa bara ett nytt formulär
        form = userProfileForm()

    # Din kod här

    return render(request, 'membership/membership.html', {'form': form})

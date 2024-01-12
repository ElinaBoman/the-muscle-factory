from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def contact(request):
    '''
    Save contact form to database and alerts user of actions outcome.
    '''
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')     
        else:    
            messages.error(request, 'Error sending message')

    else:
        return render(request, 'contact/contact.html', {'form': form})




from django import forms


# Create your models here.

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)
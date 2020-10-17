# Django is a high-level Python Web framework.
# django.forms: is a library that simplifies the creation of forms in Django
from django import forms


class ContactForm(forms.Form):
    """
     Specify as variables, the fields that compose the Contact form.
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name here'}),
                           max_length=50, required=False)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter subject here'}),
                              max_length=150, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email here'}),
                             max_length=70, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message here'}),
                              max_length=500, required=True)

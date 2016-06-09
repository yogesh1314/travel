from django import forms
#from .models import *
class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50, required = True)
    email = forms.EmailField(max_length = 100, required = True)
    contactno = forms.IntegerField(required = False)
    about = forms.CharField(max_length = 150, required = True)
    description = forms.CharField(max_length = 1500, required = True)
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
    def clean(self):
        return self.cleaned_data

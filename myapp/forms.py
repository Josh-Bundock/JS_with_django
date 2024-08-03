from django import forms 
from django.forms import ModelForm
from . models import Venue

# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'post_code', 'phone_number', 'web', 'email_address')
        labels = {
            'name' : '',
            'address' : '',
            'post_code' : '',
            'phone_number' : '',
            'web' : '',
            'email_address' : '',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name:'}),
            'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Address:'}),
            'post_code' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Post Code:'}),
            'phone_number' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Phone Number:'}), 
            'web' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Website URL:'}),
            'email_address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Email Address:'}),
        }
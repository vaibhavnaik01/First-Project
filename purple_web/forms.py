from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']       
        labels= {
            'email':'Enter Email'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'


class RegistrationForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    date_of_birth = forms.DateField(label='Date of Birth')
    email = forms.EmailField(label='Email')
    mobile_number = forms.CharField(label='Mobile Number', max_length=20)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
    occupation = forms.CharField(label='Occupation', max_length=100)
    adharcard_name = forms.CharField(label='AdharCard name', max_length=100)
    adhar_number = forms.CharField(label='Adhar Number', max_length=100)
    issued_state = forms.CharField(label='Issued State', max_length=100)
    pancard_name = forms.CharField(label='Pancard Name', max_length=100)
    pancard_number = forms.CharField(label='Pancard Number', max_length=100)
    issued_by = forms.CharField(label='Issued By', max_length=100)
    address_type = forms.CharField(label='Address Type', max_length=100)
    nationality = forms.CharField(label='Nationality', max_length=100)
    state = forms.CharField(label='State', max_length=100)
    district = forms.CharField(label='District', max_length=100)
    block_number = forms.CharField(label='Block Number', max_length=100)
    ward_number = forms.CharField(label='Ward Number', max_length=100)
    father_name = forms.CharField(label='Father Name', max_length=100)
    mother_name = forms.CharField(label='Mother Name', max_length=100)
    spouse_name = forms.CharField(label='Spouse Name', max_length=100)
    sibling_name = forms.CharField(label='Brother/Sister Name', max_length=100)


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # first_name = forms.CharField(max_length=25)
    # last_name = forms.CharField(max_length=25)
    class Meta:
        model = User

        fields = ['username', 'email' ]

        # fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if email.split('@')[-1] !=  'gmail.com':
            raise forms.ValidationError("Only @gmail.com email addresses allowed")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("User with that email already exists")
        # r = User.objects.filter(email=email)
        #     if r.count():
        return email
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['image',
                    'date_of_birth',
                    'country',
                    'date_of_birth',
                    'address1',
                    'address2',
                    'zip_code',
                    'city',
                    'occupation',
                    'mobile_phone',
                    'portfolio_site',


                    # 'additional_information'

                    ]
        widgets = {
                'date_of_birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            }

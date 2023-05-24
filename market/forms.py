from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm) :
    # do some configuration
    class Meta:
        model = User
        # define the fields we want to have on the form to sign up
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Your user name",
        'class' : "w-full py-4 px-6 rounded-xl"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : "Your Email Adress",
        'class' : "w-full py-4 px-6 rounded-xl"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : "Your Password",
        'class' : "w-full py-4 px-6 rounded-xl"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : "Confirm Your Password",
        'class' : "w-full py-4 px-6 rounded-xl"
    }))


# define the authentication form 
class LoginForm(AuthenticationForm) :

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter you user name',
        'class' : "w-full py-4 px-6 rounded-xl"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Your Password',
        'class' : "w-full py-4 px-6 rounded-xl"
    }))
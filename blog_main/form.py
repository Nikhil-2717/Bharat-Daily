from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model= User  # that means what will be model we want to display
        fields = ('email','username','password1','password2') #these are teh fields which will be dispalyed on the register page 
        
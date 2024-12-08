from .models import User
from django.forms import ModelForm

class Signup_form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number','age','gender','address','password']

class Profile_edit_form(ModelForm):
    class Meta:
        model = User
        fields = ['email','phone_number','age','gender','address','dp']
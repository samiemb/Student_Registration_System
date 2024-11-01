from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone_number', 'date_of_birth', 'address',
                  'is_student', 'is_instructor', 'major', 'student_id', 'profile_picture')
        widgets = {
            'password': forms.PasswordInput(),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'date_of_birth', 'address', 'profile_picture']
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

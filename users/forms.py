from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
        email = forms.EmailField(label='Email address')
        first_name = forms.CharField(max_length=30, required=True, help_text='Required.')

        class Meta:
            model = User
            fields = ('email', 'first_name', 'password1', 'password2')
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.username = self.cleaned_data['email']
            if commit:
                user.save()
            return user
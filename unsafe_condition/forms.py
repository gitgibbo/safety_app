from django import forms
from .models import UnsafeCondition

class UnsafeConditionForm(forms.ModelForm):
    class Meta:
        model = UnsafeCondition
        fields = ['location', 'description', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'photo': forms.FileInput(),
        }
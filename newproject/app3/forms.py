from django import forms
from.models import tab
class todoform(forms.ModelForm):
    class Meta:
        model=tab
        fields=['title']
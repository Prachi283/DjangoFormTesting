from django import forms 
from .models import Employee
# creating a form 
class Createform(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

from dataclasses import field
from pyexpat import model
from django import forms
from .models import TDepartments, TEmployees

class DepForm(forms.ModelForm):

    class Meta:
        model = TDepartments
        fields = ('__all__')

class EmpForm(forms.ModelForm):

    class Meta:
        model = TEmployees
        fields = ('__all__')